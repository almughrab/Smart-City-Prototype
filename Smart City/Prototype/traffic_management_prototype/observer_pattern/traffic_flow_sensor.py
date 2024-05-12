from observer_pattern.observer import Observer


class TrafficFlowSensor(Observer):
    def __init__(self, signal):
        self.signal = signal
        self.traffic_flow_data = {}

    def update(self):
        # In a real implementation, this method would collect traffic flow data
        for road, flow_data in self.traffic_flow_data.items():
            print(f"Traffic flow data for {road}: {flow_data}")

    def collect_traffic_flow_data(self, road, flow_data):
        # Simulate realistic traffic flow data collection
        # Factors such as time of day, road type, weather conditions, etc., can influence traffic flow
        # Here, we simply update the flow data for the specified road
        if road in self.traffic_flow_data:
            self.traffic_flow_data[road].append(flow_data)
        else:
            self.traffic_flow_data[road] = [flow_data]
