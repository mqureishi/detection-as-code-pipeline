#!/usr/bin/env python3
import os
import sys
import yaml

RULES_DIR = "rules"
MANDATORY_KEYS = ["title", "id", "status", "logsource", "detection"]

def validate_detection_rules():
    print("[*] Starting Advanced Detection-as-Code (DaC) Governance & Syntax Validation...")
    
    if not os.path.exists(RULES_DIR):
        print(f"[!] Error: Rules directory '{RULES_DIR}' not found.")
        sys.exit(1)
        
    rule_files = [f for f in os.listdir(RULES_DIR) if f.endswith(".yml") or f.endswith(".yaml")]
    
    if not rule_files:
        print("[!] Warning: No detection rule files found to validate.")
        sys.exit(0)
        
    validation_failed = False

    for file_name in rule_files:
        file_path = os.path.join(RULES_DIR, file_name)
        print(f"[-] Inspecting rule file: {file_name}")
        
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                rule_data = yaml.safe_load(f)
        except yaml.YAMLError as exc:
            print(f"    [X] YAML Syntax Error in {file_name}: {exc}")
            validation_failed = True
            continue
        except Exception as e:
            print(f"    [X] Unexpected error reading {file_name}: {e}")
            validation_failed = True
            continue
            
        if not isinstance(rule_data, dict):
            print(f"    [X] Structure Error: {file_name} does not contain a valid YAML dictionary mapping.")
            validation_failed = True
            continue
            
        # 1. Check for mandatory keys
        missing_keys = [key for key in MANDATORY_KEYS if key not in rule_data]
        if missing_keys:
            print(f"    [X] Schema Error in {file_name}: Missing mandatory keys -> {missing_keys}")
            validation_failed = True
        else:
            print(f"    [OK] Mandatory structural keys present.")

        # 2. Advanced Governance: Check for MITRE ATT&CK tags
        tags = rule_data.get("tags", [])
        has_mitre_tag = any(tag.startswith("attack.t") for tag in tags)
        
        if not has_mitre_tag:
            print(f"    [X] Governance Error in {file_name}: Rule lacks a valid MITRE ATT&CK technique tag (e.g., 'attack.t1033').")
            validation_failed = True
        else:
            print(f"    [OK] Valid MITRE ATT&CK technique tag detected.")

    if validation_failed:
        print("\n[!] Validation FAILED. Please fix the rule errors listed above.")
        sys.exit(1)
    else:
        print("\n[SUCCESS] All detection rules passed advanced governance and syntax validation!")
        sys.exit(0)

if __name__ == "__main__":
    validate_detection_rules()
