import matplotlib.pyplot as plt

class Visualization:
    @staticmethod
    def plot_sensitivity_matrix(data, output_path):
        """
        Plot sensitivity matrix as a heatmap.
        """
        fig, ax = plt.subplots()
        cax = ax.matshow(data, cmap="coolwarm")
        plt.colorbar(cax)
        plt.savefig(output_path)

    @staticmethod
    def plot_cash_flows(cash_flows, output_path):
        """
        Plot cash flows over time.
        """
        plt.figure(figsize=(10, 6))
        plt.bar(range(len(cash_flows)), cash_flows)
        plt.savefig(output_path)
