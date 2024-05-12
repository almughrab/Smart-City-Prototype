from simulation.traffic_simulation import TrafficSimulation
from visualization.traffic_visualization import TrafficVisualization
import threading

def main():
    simulation = TrafficSimulation()
    visualization = TrafficVisualization(simulation)

    # Create roads and vehicles
    simulation.add_road("A", 10)
    simulation.add_road("B", 15)
    simulation.add_road("C", 12)
    simulation.add_vehicle(1, "A", 1)
    simulation.add_vehicle(2, "B", 1)
    simulation.add_vehicle(3, "C", 1)

    try:
        # Start simulation thread
        simulation_thread = threading.Thread(target=simulation.simulate)
        simulation_thread.start()

        # Visualize simulation
        while True:
            visualization.visualize()

    except KeyboardInterrupt:
        simulation.stop()

if __name__ == "__main__":
    main()
