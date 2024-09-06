import customtkinter as ctk
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Plotter:
    def __init__(self, master):
        self.master = master

    def plot_normal_distribution(self, z_score, mean, std_dev):
        # Clear the previous plot
        for widget in self.master.winfo_children():
            widget.destroy()

        # Generate x values from mean-3*std_dev to mean+3*std_dev
        x = np.linspace(mean - 3 * std_dev, mean + 3 * std_dev, 1000)
        # Generate y values based on the normal distribution
        y = norm.pdf(x, mean, std_dev)

        # Create the plot
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.plot(x, y, label='Normal Distribution')
        ax.fill_between(x, y, where=(x <= mean + z_score * std_dev), color='skyblue', alpha=0.4, label='Area under the curve')
        ax.axvline(mean + z_score * std_dev, color='r', linestyle='--', label=f'Z-score = {z_score:.2f}')

        # Set x-axis limits based on mean and standard deviation
        ax.set_xlim(mean - 3 * std_dev, mean + 3 * std_dev)

        # Customize x-axis ticks to show number of standard deviations from the mean
        ticks = np.arange(mean - 3 * std_dev, mean + 3 * std_dev + 1, std_dev)
        tick_labels = [f'{int((t - mean) / std_dev)}.0' for t in ticks]
        ax.set_xticks(ticks)
        ax.set_xticklabels(tick_labels)

        ax.set_title('Normal Distribution')
        ax.set_xlabel('Standard Deviations from Mean')
        ax.set_ylabel('Probability Density')
        ax.legend()
        ax.grid(True)

        # Embed the plot in the Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=self.master)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=ctk.BOTH, expand=True)