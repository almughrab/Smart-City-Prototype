# dashboard.py
import tkinter as tk
from tkinter import ttk

class Dashboard:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Waste Management Dashboard")

        # Strategy display label
        self.strategy_label = ttk.Label(self.root, text="Selected Waste Disposal Strategy:")
        self.strategy_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        # Sensor data display label
        self.sensor_data_label = ttk.Label(self.root, text="Sensor Data:")
        self.sensor_data_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        # Sensor data display text widget
        self.sensor_data_text = tk.Text(self.root, width=40, height=10)
        self.sensor_data_text.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

    def display_strategy(self, strategy_name):
        # Update strategy label
        self.strategy_label.config(text="Selected Waste Disposal Strategy: " + strategy_name)

    def display_sensor_data(self, sensor_data):
        # Clear previous sensor data
        self.sensor_data_text.delete(1.0, tk.END)
        # Display new sensor data
        for sensor, data in sensor_data.items():
            self.sensor_data_text.insert(tk.END, sensor + ": " + str(data) + "\n")

    def run(self):
        self.root.mainloop()
