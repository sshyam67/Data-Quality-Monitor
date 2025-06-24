import yaml

class RuleEngine:
    def __init__(self, config_path):
        with open(config_path) as f:
            self.rules = yaml.safe_load(f)["rules"]

    def validate(self, df):
        issues = []
        for rule in self.rules:
            col = rule["column"]
            check = rule["check"]

            if check == "not_null" and df[col].isnull().any():
                issues.append(f"{col} has nulls")
            elif check == "unique" and df[col].duplicated().any():
                issues.append(f"{col} contains duplicates")
            elif check == "no_negative" and (df[col] < 0).any():
                issues.append(f"{col} has negative values")
            elif check == "date_format":
                fmt = rule.get("format", "%Y-%m-%d")
                try:
                    pd.to_datetime(df[col], format=fmt)
                except:
                    issues.append(f"{col} has incorrect date format")
        return issues
