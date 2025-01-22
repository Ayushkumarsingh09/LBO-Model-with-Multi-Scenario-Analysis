from src.lbo_model import LBOModel

class ScenarioAnalysis:
    def __init__(self, base_assumptions, scenarios):
        """
        Initialize scenario analysis.
        :param base_assumptions: Dictionary of base assumptions.
        :param scenarios: Dictionary of scenarios with adjustment values.
        """
        self.base_assumptions = base_assumptions
        self.scenarios = scenarios

    def run_scenarios(self, financials):
        """
        Run the LBO model across different scenarios.
        :param financials: Dictionary containing financial data.
        :return: Dictionary of scenario results.
        """
        results = {}
        for name, adjustments in self.scenarios.items():
            assumptions = {**self.base_assumptions, **adjustments}
            model = LBOModel(financials, assumptions)
            results[name] = model.run_model()
        return results
