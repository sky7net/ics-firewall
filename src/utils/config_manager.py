import os
import json

# Mutlak dosya yollarını ayarla
BASE_DIR = os.path.dirname(__file__)
CONFIG_PATH = os.path.abspath(os.path.join(BASE_DIR, '..', 'config', 'firewall_config.json'))
RULES_PATH = os.path.abspath(os.path.join(BASE_DIR, '..', 'config', 'rules.json'))

def load_config():
    """
    Konfigürasyon dosyasını yükler.
    
    :return: dict - Konfigürasyon ayarları
    """
    try:
        with open(CONFIG_PATH, 'r') as file:
            config = json.load(file)
        print(f"Configuration loaded from {CONFIG_PATH}.")
        return config
    except FileNotFoundError:
        print(f"Config dosyası bulunamadı: {CONFIG_PATH}")
        return {}

def update_config(new_config):
    """
    Yeni konfigürasyon ayarlarını dosyaya kaydeder.
    
    :param new_config: Güncellenmiş konfigürasyon
    """
    with open(CONFIG_PATH, 'w') as file:
        json.dump(new_config, file, indent=4)
    print(f"Configuration updated in {CONFIG_PATH}.")

def load_rules():
    """
    Kurallar dosyasını yükler.
    
    :return: list - Kurallar listesi
    """
    try:
        with open(RULES_PATH, 'r') as file:
            rules = json.load(file)
        print(f"Rules loaded from {RULES_PATH}.")
        return rules
    except FileNotFoundError:
        print(f"Rules dosyası bulunamadı: {RULES_PATH}")
        return []

def save_rules(rules):
    """
    Güncellenmiş kuralları dosyaya kaydeder.
    
    :param rules: Güncellenmiş kurallar listesi
    """
    with open(RULES_PATH, 'w') as file:
        json.dump(rules, file, indent=4)
    print(f"Rules updated in {RULES_PATH}.")
