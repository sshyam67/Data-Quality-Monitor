from src.data_validator import DataValidator

if __name__ == "__main__":
    validator = DataValidator("data/sample_data.csv", "config/rules_config.yaml")
    validator.run_checks()
