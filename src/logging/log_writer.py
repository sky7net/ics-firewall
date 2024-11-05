from datetime import datetime
import os

class LogWriter:
    """
    Firewall için loglama işlemlerini yöneten sınıf.
    """

    def __init__(self, log_path='logging/firewall_logs.txt'):
        # Log dosyasının yolu
        self.log_path = log_path
        os.makedirs(os.path.dirname(self.log_path), exist_ok=True)  # Klasörü oluştur

    def log(self, message):
        """
        Log mesajını dosyaya yazar.
        
        :param message: Loglanacak mesaj
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.log_path, 'a') as file:
            file.write(f"{timestamp} - {message}\n")
        print(f"{timestamp} - {message}")
