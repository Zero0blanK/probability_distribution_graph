import customtkinter as ctk
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from Calculator import Calculator
from Plotter import Plotter

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Normal Distribution Calculator")
        self.root.geometry("1440x700")

        self.calculator = Calculator()
        self.plotter = Plotter(self.create_plot_frame())

        self.create_input_frame()
        self.create_result_frame()

        # Configure grid row and column weights
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=0)  # Left column (input and result)

    def create_input_frame(self):
        # Create and place the input fields on the left side
        input_frame = ctk.CTkFrame(self.root, corner_radius=20)
        input_frame.grid(row=0, column=0, padx=20, pady=20, ipady=30, rowspan=1, sticky="nwe")

        raw_score_label = ctk.CTkLabel(input_frame, text="Enter raw score:")
        raw_score_label.grid(row=0, column=0, padx=10, pady=10)
        self.raw_score_entry = ctk.CTkEntry(input_frame)
        self.raw_score_entry.grid(row=0, column=1, padx=10, pady=10)

        mean_label = ctk.CTkLabel(input_frame, text="Enter mean:")
        mean_label.grid(row=1, column=0, padx=10, pady=10)
        self.mean_entry = ctk.CTkEntry(input_frame)
        self.mean_entry.grid(row=1, column=1, padx=10, pady=10)

        std_dev_label = ctk.CTkLabel(input_frame, text="Enter standard deviation:")
        std_dev_label.grid(row=2, column=0, padx=10, pady=10)
        self.std_dev_entry = ctk.CTkEntry(input_frame)
        self.std_dev_entry.grid(row=2, column=1, padx=10, pady=10)

        calculate_button = ctk.CTkButton(input_frame, text="Calculate", command=self.calculate)
        calculate_button.grid(row=3, column=0, columnspan=2, pady=20)

    def create_result_frame(self):
        # Create a separate result frame below the input frame
        result_frame = ctk.CTkFrame(self.root, corner_radius=20)
        result_frame.grid(row=1, column=0, padx=20, pady=20, ipady=70, rowspan=1, sticky="nsew")

        # Create and configure the z_score_label
        self.z_score_label = ctk.CTkLabel(result_frame, text="", font=("Arial", 14))
        self.z_score_label.grid(row=0, column=0, pady=10, sticky="ew")
        self.z_score_label.grid_columnconfigure(0, weight=1)
        self.z_score_label.configure(anchor="center")

        # Create and configure the area_label
        self.area_label = ctk.CTkLabel(result_frame, text="", font=("Arial", 14))
        self.area_label.grid(row=1, column=0, pady=10, sticky="ew")
        self.area_label.grid_columnconfigure(0, weight=1)
        self.area_label.configure(anchor="center")

    def create_plot_frame(self):
        # Create and place the plot frame on the right side
        plot_frame = ctk.CTkFrame(self.root, corner_radius=20)
        plot_frame.grid(row=0, column=1, rowspan=2, padx=20, pady=20, sticky="nsew")
        return plot_frame

    def calculate(self):
        try:
            # Get inputs from the user
            raw_score = float(self.raw_score_entry.get())
            mean = float(self.mean_entry.get())
            std_dev = float(self.std_dev_entry.get())

            # Set values in the calculator
            self.calculator.set_values(raw_score, mean, std_dev)

            # Calculate z-score and area percentage
            z_score = self.calculator.calculate_z_score()
            area_percentage = self.calculator.calculate_area_percentage()

            # Update the results in the GUI
            self.z_score_label.configure(text=f"Z-score: {z_score:.4f}")
            self.area_label.configure(text=f"Area under the curve (percentage): {area_percentage:.2f}%")

            # Plot the distribution
            self.plotter.plot_normal_distribution(z_score, mean, std_dev)

        except ValueError:
            self.z_score_label.configure(text="Invalid input. Please enter numeric values.")
            self.area_label.configure(text="")

# Set the appearance mode and color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Main window
root = ctk.CTk()
app = MainApp(root)
root.mainloop()