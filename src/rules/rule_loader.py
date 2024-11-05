import json

RULES_PATH = "config/rules.json"

def load_rules():
    """
    Kural dosyasını yükler ve kuralları döndürür.
    
    :return: list - Yüklenmiş kuralların listesi
    """
    with open(RULES_PATH, 'r') as file:
        rules = json.load(file)
    print(f"{len(rules)} rules loaded from {RULES_PATH}.")
    return rules
