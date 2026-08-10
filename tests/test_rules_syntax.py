import os
import yaml

RULES_DIR = "rules"

def test_yaml_syntax():
    """Iterates through all YAML files in the rules directory and validates their syntax and required fields."""
    print("[*] Starting Detection-as-Code Rule Validation...")
    
    # Check if the rules directory exists
    if not os.path.exists(RULES_DIR):
        raise FileNotFoundError(f"[-] Critical Error: The '{RULES_DIR}' directory does not exist.")

    rule_files = [f for f in os.listdir(RULES_DIR) if f.endswith(".yml") or f.endswith(".yaml")]
    
    if not rule_files:
        print("[!] Warning: No detection rule files found to test.")
        return

    failed = False
    for file_name in rule_files:
        file_path = os.path.join(RULES_DIR, file_name)
        print(f"[*] Validating rule file: {file_name}")
        
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                rule_data = yaml.safe_load(f)
                
            # Basic schema validation checks for required fields
            required_fields = ["title", "id", "status", "logsource", "detection"]
            for field in required_fields:
                if field not in rule_data:
                    print(f"    [-] Validation Failed: Missing required field '{field}' in {file_name}")
                    failed = True
                else:
                    print(f"    [+] Found required field: '{field}'")
                    
        except yaml.YAMLError as exc:
            print(f"    [-] YAML Syntax Error in {file_name}: {exc}")
            failed = True

    if failed:
        raise AssertionError("[-] Rule validation failed due to schema or syntax errors.")
    else:
        print("[+] Success: All detection rules passed syntax and schema validation!")

if __name__ == "__main__":
    test_yaml_syntax()
