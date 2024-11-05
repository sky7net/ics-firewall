import os

def get_latest_logs(limit=50):
    """
    Son logları alır.
    
    :param limit: Gösterilecek maksimum log sayısı
    :return: list - Log mesajları listesi
    """
    logs = []
    
    # Mutlak dosya yolunu oluştur
    log_path = os.path.join(os.path.dirname(__file__), '..', 'logging', 'firewall_logs.txt')
    log_path = os.path.abspath(log_path)
    
    # Dosyayı aç ve son `limit` kadar logu oku
    try:
        with open(log_path) as file:
            for line in file.readlines()[-limit:]:
                logs.append(line.strip())
        print(f"{limit} latest logs fetched.")
    except FileNotFoundError:
        print(f"Log dosyası bulunamadı: {log_path}")
    
    return logs
