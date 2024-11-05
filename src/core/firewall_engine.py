from rules.rule_manager import RuleManager
from logging.log_writer import LogWriter

class FirewallEngine:
    def __init__(self):
        self.rule_manager = RuleManager()
        self.logger = LogWriter()

    def evaluate_packet(self, packet):
        try:
            # Anomali tespiti
            if self.rule_manager.check_anomaly(packet):
                self.logger.log(f"[DYNAMIC BLOCK] Anomalous behavior detected. Blocking IP: {packet['source']}")

            # Kural eşleştirme
            rule = self.rule_manager.find_matching_rule(packet)
            if rule and rule.get('action') == 'allow':
                self.logger.log(f"[ALLOW] Packet allowed: {packet}")
                return True
            else:
                self.logger.log(f"[BLOCK] Packet blocked: {packet}")
                return False
        except Exception as e:
            self.logger.log(f"[ERROR] Exception during packet evaluation: {str(e)}")
            return False
