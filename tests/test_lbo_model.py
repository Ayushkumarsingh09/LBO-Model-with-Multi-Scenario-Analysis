import unittest
from src.lbo_model import LBOModel

class TestLBOModel(unittest.TestCase):
    def test_equity_irr(self):
        financials = {"EBITDA": [5000000, 5500000], "CapEx": [200000, 220000], "WorkingCapitalChange": [50000, 55000]}
        assumptions = {"InitialDebt": 2000000, "EquityContribution": 1000000, "ExitMultiple": 8.0}
        model = LBOModel(financials, assumptions)
        results = model.run_model()
        self.assertGreater(results["EquityIRR"], 0)
