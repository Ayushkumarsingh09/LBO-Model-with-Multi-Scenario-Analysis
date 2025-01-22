import numpy as np

class LBOModel:
    def __init__(self, financials, assumptions):
        """
        Initialize the LBO model.
        :param financials: Dictionary containing financial data.
        :param assumptions: Dictionary containing LBO assumptions.
        """
        self.financials = financials
        self.assumptions = assumptions
        self.results = {}

    def calculate_debt_repayment(self):
        """
        Calculate yearly debt repayment based on cash available and remaining debt.
        """
        cash_available = self.financials["EBITDA"] - self.financials["CapEx"] - self.financials["WorkingCapitalChange"]
        debt_balance = self.assumptions["InitialDebt"]
        debt_repayment = []

        for cash in cash_available:
            repayment = min(cash, debt_balance)
            debt_balance -= repayment
            debt_repayment.append(repayment)

        self.results["DebtRepayment"] = debt_repayment
        self.results["RemainingDebt"] = debt_balance

    def calculate_equity_irr(self):
        """
        Calculate the equity internal rate of return (IRR).
        """
        exit_value = self.financials["EBITDA"][-1] * self.assumptions["ExitMultiple"]
        equity_investment = self.assumptions["EquityContribution"]
        cash_flows = [-equity_investment] + [0] * (len(self.results["DebtRepayment"]) - 1) + [exit_value]
        irr = np.irr(cash_flows)
        self.results["EquityIRR"] = irr

    def run_model(self):
        """
        Run the LBO model and return results.
        """
        self.calculate_debt_repayment()
        self.calculate_equity_irr()
        return self.results
