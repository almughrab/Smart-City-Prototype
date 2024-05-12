import time
import random
from observer_pattern.traffic_signal import TrafficSignal
from observer_pattern.traffic_flow_sensor import TrafficFlowSensor
from simulation.road import Road
from simulation.intersection import Intersection
from simulation.vehicle import Vehicle

class TrafficSimulation:
    def __init__(self):
        self.roads = {}
        self.intersections = {}
        self.vehicles = {}
        self.running = False
        self.signal = TrafficSignal()
        self.flow_sensor = TrafficFlowSensor(self.signal)

    def add_road(self, name, length):
        road = Road(name, length)
        self.roads[name] = road
        return road

    def add_intersection(self, name):
        intersection = Intersection(name)
        self.intersections[name] = intersection
        return intersection

    def add_vehicle(self, id, road_name, speed):
        road = self.roads.get(road_name)
        if road:
            vehicle = Vehicle(id, road, speed)
            road.add_vehicle(vehicle)
            self.vehicles[id] = vehicle

    def update_traffic_signal(self):
        # Simulate traffic flow data collection for each road
        for road_name, road in self.roads.items():
            flow_data = random.randint(10, 100)  # Simulate flow data
            self.flow_sensor.collect_traffic_flow_data(road_name, flow_data)

        # Determine optimal signal state based on traffic flow data
        signal_state = self.determine_signal_state()
        self.signal.change_signal(signal_state)

    def determine_signal_state(self):
        # In a real implementation, this method would analyze traffic flow data
        # and additional factors (e.g., time of day, road conditions) to determine the optimal signal state
        # For simplicity, let's assume a basic heuristic for now
        total_flow = sum(sum(flow_data) for flow_data in self.flow_sensor.traffic_flow_data.values())
        average_flow = total_flow / len(self.vehicles)
        if average_flow > 50:
            return "Green"
        else:
            return "Red"

    def simulate(self):
        self.running = True
        while self.running:
            self.update_traffic_signal()
            for vehicle_id, vehicle in self.vehicles.items():
                road = vehicle.get_road()
                road_length = road.get_length()
                if vehicle.get_position() >= road_length:
                    road.remove_vehicle(vehicle)
                    del self.vehicles[vehicle_id]
                else:
                    vehicle.move()
            time.sleep(1)  # Adjust simulation speed as needed
