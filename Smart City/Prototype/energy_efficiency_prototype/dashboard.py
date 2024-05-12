import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

class DashboardApp:
    def __init__(self, energy_management):
        self.energy_management = energy_management

        self.root = tk.Tk()
        self.root.title("Energy Efficiency Dashboard")

        # Create GUI elements and layout
        self.label = tk.Label(self.root, text="Real-time Energy Consumption")
        self.label.pack()

        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Energy Consumption")
        self.ax.set_title("Energy Consumption Trend")
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Add a dropdown menu to select visualization type
        self.visualization_type_var = tk.StringVar()
        self.visualization_type_var.set("Line Plot")
        self.visualization_type_menu = ttk.OptionMenu(self.root, self.visualization_type_var, "Line Plot", "Bar Chart", "Pie Chart", command=self.update_visualization)
        self.visualization_type_menu.pack()

        # Fetch and display real-time data
        self.fetch_real_time_data()

    def fetch_real_time_data(self):
        # Method to fetch real-time energy consumption data
        # For demonstration, generate random data
        sectors = ["Residential", "Commercial", "Industrial"]
        energy_data = {sector: random.randint(100, 1000) for sector in sectors}
        self.update_visualization(energy_data)

    def update_visualization(self, energy_data):
        # Method to update the visualization based on selected type
        visualization_type = self.visualization_type_var.get()
        self.ax.clear()
        if visualization_type == "Line Plot":
            self.ax.plot(list(energy_data.keys()), list(energy_data.values()), marker='o', color='b')
        elif visualization_type == "Bar Chart":
            self.ax.bar(list(energy_data.keys()), list(energy_data.values()), color='b')
        elif visualization_type == "Pie Chart":
            self.ax.pie(list(energy_data.values()), labels=list(energy_data.keys()), autopct='%1.1f%%', startangle=140)
        self.ax.set_xlabel("Sector")
        self.ax.set_ylabel("Energy Consumption")
        self.ax.set_title("Real-time Energy Consumption")
        self.canvas.draw()

    def run(self):
        self.root.mainloop()
