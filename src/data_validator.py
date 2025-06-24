import pandas as pd
from src.rule_engine import RuleEngine
from src.alert_manager import AlertManager

class DataValidator:
    def __init__(self, filepath, config_path):
        self.data = pd.read_csv(filepath)
        self.engine = RuleEngine(config_path)
        self.alert = AlertManager()

    def run_checks(self):
        results = self.engine.validate(self.data)
        for issue in results:
            self.alert.send_alert(issue)
        print("Validation completed.")
