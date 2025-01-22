class ReportGenerator:
    @staticmethod
    def generate_summary(results, output_path):
        """
        Generate a summary text report of LBO results.
        """
        with open(output_path, "w") as f:
            f.write("LBO Summary Report\n")
            f.write("-------------------\n")
            f.write(f"Equity IRR: {results['EquityIRR']:.2%}\n")
            f.write(f"Remaining Debt: {results['RemainingDebt']}\n")
