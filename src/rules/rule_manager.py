from rules.rule_loader import load_rules
from datetime import datetime, timedelta

class RuleManager:
    def __init__(self):
        self.rules = load_rules()
        self.dynamic_rules = []
        self.connection_count = {}
        self.anomaly_threshold = 100  # Belirli bir süre içinde 100'den fazla bağlantı yapılırsa tetiklenir
        self.anomaly_time_window = timedelta(minutes=1)

    def add_dynamic_rule(self, source_ip, action="block"):
        """
        Dinamik bir kural ekler (örneğin, çok fazla bağlantı yapan IP’yi engelle).
        """
        self.dynamic_rules.append({
            "source": source_ip,
            "action": action,
            "timestamp": datetime.now()
        })

    def find_matching_rule(self, packet):
        # Statik kurallara göre eşleştirme
        for rule in self.rules + self.dynamic_rules:
            if rule['source'] == packet['source'] and rule.get('destination') == packet.get('destination'):
                return rule
        return None

    def check_anomaly(self, packet):
        """
        Anomalileri kontrol eder. Belirli bir IP çok fazla bağlantı yapıyorsa bu IP için kural ekler.
        """
        source = packet['source']
        now = datetime.now()
        
        if source not in self.connection_count:
            self.connection_count[source] = []
        
        self.connection_count[source].append(now)
        # Zaman penceresi dışındaki eski bağlantıları kaldırıyoruz
        self.connection_count[source] = [time for time in self.connection_count[source] if now - time <= self.anomaly_time_window]

        if len(self.connection_count[source]) > self.anomaly_threshold:
            print(f"[ANOMALY DETECTED] Too many connections from {source}. Adding dynamic block rule.")
            self.add_dynamic_rule(source)
            return True
        return False
