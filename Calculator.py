import customtkinter as ctk
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Calculator:
    def __init__(self):
        self.raw_score = 0.0
        self.mean = 0.0
        self.std_dev = 1.0

    def set_values(self, raw_score, mean, std_dev):
        self.raw_score = raw_score
        self.mean = mean
        self.std_dev = std_dev

    def calculate_z_score(self):
        return (self.raw_score - self.mean) / self.std_dev

    def calculate_area_percentage(self):
        z_score = self.calculate_z_score()
        return norm.cdf(z_score) * 100
