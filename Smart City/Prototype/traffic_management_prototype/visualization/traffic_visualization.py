import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class TrafficVisualization:
    def __init__(self, simulation):
        self.simulation = simulation
        self.fig, self.ax = plt.subplots()
        self.road_colors = {'A': 'blue', 'B': 'green', 'C': 'red'}
        self.vehicle_markers = ['o', 's', '^', 'D']

    def update_plot(self, frame):
        self.ax.clear()

        # Plot roads
        for road_name, road in self.simulation.roads.items():
            road_length = road.get_length()
            self.ax.plot([0, road_length], [0, 0], color=self.road_colors.get(road_name), linewidth=3)
            self.ax.text(road_length / 2, -1, road_name, ha='center', fontsize=12)

        # Plot vehicles
        for road_name, road in self.simulation.roads.items():
            vehicles = road.get_vehicles()
            for i, vehicle in enumerate(vehicles):
                vehicle_pos = vehicle.get_position()
                self.ax.plot(vehicle_pos, 0, marker=self.vehicle_markers[i % len(self.vehicle_markers)], color=self.road_colors.get(road_name), markersize=10)

        # Plot traffic signal state
        signal_state = self.simulation.signal_state
        self.ax.text(0, 2, f"Traffic Signal: {signal_state}", fontsize=12)

        # Customize plot
        self.ax.set_xlim(-1, max([road.get_length() for road in self.simulation.roads.values()]) + 1)
        self.ax.set_ylim(-2, 3)
        self.ax.set_aspect('equal')
        self.ax.axis('off')

    def visualize(self):
        animation = FuncAnimation(self.fig, self.update_plot, interval=1000)  # Update plot every 1 second
        plt.show()
