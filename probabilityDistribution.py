import tkinter as tk
from tkinter import ttk
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def calculate():

    try:
        # Get inputs from the user
        raw_score = float(raw_score_entry.get())
        mean = float(mean_entry.get())
        std_dev = float(std_dev_entry.get())

        # Calculate the z-score
        z_score = (raw_score - mean) / std_dev
        area = norm.cdf(z_score)
        area_percentage = area * 100

        # Update the results in the GUI
        z_score_label.config(text=f"Z-score: {z_score:.4f}")
        area_label.config(text=f"Area under the curve (percentage): {area_percentage:.2f}%")

        # Plot the distribution
        plot_normal_distribution(z_score, mean, std_dev)

    except ValueError:
        z_score_label.config(text="Invalid input. Please enter numeric values.")
        area_label.config(text="")


def plot_normal_distribution(z_score, mean, std_dev):
    
    # Clear the previous plot
    for widget in plot_frame.winfo_children():
        widget.destroy()

    # Generate x values from mean-3*std_dev to mean+3*std_dev
    x = np.linspace(mean - 3*std_dev, mean + 3*std_dev, 1000)

    # Generate y values based on the normal distribution
    y = norm.pdf(x, mean, std_dev)


    # Create the plot
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(x, y, label='Normal Distribution')
    ax.fill_between(x, y, where=(x <= mean + z_score*std_dev), color='skyblue', alpha=0.4, label='Area under the curve')
    ax.axvline(mean + z_score*std_dev, color='r', linestyle='--', label=f'Z-score = {z_score:.2f}')

    # Set x-axis limits based on mean and standard deviation
    ax.set_xlim(mean - 3*std_dev, mean + 3*std_dev)

    # Customize x-axis ticks to show number of standard deviations from the mean
    ticks = np.arange(mean - 3*std_dev, mean + 3*std_dev + 1, std_dev)
    tick_labels = [f'{int((t - mean) / std_dev)}.0' for t in ticks]
    ax.set_xticks(ticks)
    ax.set_xticklabels(tick_labels)
    ax.set_title('Normal Distribution')
    ax.set_xlabel('Standard Deviations from Mean')
    ax.set_ylabel('Probability Density')
    ax.legend()
    ax.grid(True)

    # Embed the plot in the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Create the main window
root = tk.Tk()
root.title("Normal Distribution Calculator")

# Create and place the input fields
input_frame = ttk.Frame(root, padding="10")
input_frame.grid(row=0, column=0, padx=10, pady=10)
    
raw_score_label = ttk.Label(input_frame, text="Enter raw score:")
raw_score_label.grid(row=0, column=0, padx=5, pady=5)
raw_score_entry = ttk.Entry(input_frame)
raw_score_entry.grid(row=0, column=1, padx=5, pady=5)


mean_label = ttk.Label(input_frame, text="Enter mean:")
mean_label.grid(row=1, column=0, padx=5, pady=5)
mean_entry = ttk.Entry(input_frame)
mean_entry.grid(row=1, column=1, padx=5, pady=5)


std_dev_label = ttk.Label(input_frame, text="Enter standard deviation:")
std_dev_label.grid(row=2, column=0, padx=5, pady=5)
std_dev_entry = ttk.Entry(input_frame)
std_dev_entry.grid(row=2, column=1, padx=5, pady=5)

calculate_button = ttk.Button(input_frame, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)


# Create and place the result labels
result_frame = ttk.Frame(root, padding="10")
result_frame.grid(row=1, column=0, padx=10, pady=10)

z_score_label = ttk.Label(result_frame, text="")
z_score_label.grid(row=0, column=0, pady=5)

area_label = ttk.Label(result_frame, text="")
area_label.grid(row=1, column=0, pady=5)


# Create and place the plot frame
plot_frame = ttk.Frame(root)
plot_frame.grid(row=2, column=0, padx=10, pady=10, sticky=tk.NSEW)

# Configure grid row and column weights
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)

# Start the Tkinter event loop
root.mainloop()