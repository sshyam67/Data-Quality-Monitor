import unittest
import pandas as pd
from src.rule_engine import RuleEngine

class TestValidator(unittest.TestCase):
    def test_not_null(self):
        df = pd.DataFrame({"age": [25, None]})
        engine = RuleEngine("config/rules_config.yaml")
        results = engine.validate(df)
        self.assertIn("age has nulls", results)

if __name__ == '__main__':
    unittest.main()
