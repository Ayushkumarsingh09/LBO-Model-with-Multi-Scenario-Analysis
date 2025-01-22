import unittest
from src.financial_calculations import calculate_enterprise_value, calculate_equity_value

class TestFinancialCalculations(unittest.TestCase):
    def test_enterprise_value(self):
        ebitda = 5000000
        multiple = 10
        ev = calculate_enterprise_value(ebitda, multiple)
        self.assertEqual(ev, 50000000)

    def test_equity_value(self):
        ev = 50000000
        net_debt = 10000000
        equity_value = calculate_equity_value(ev, net_debt)
        self.assertEqual(equity_value, 40000000)
