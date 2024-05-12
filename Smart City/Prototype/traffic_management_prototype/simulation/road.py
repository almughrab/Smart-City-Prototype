class Road:
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def remove_vehicle(self, vehicle):
        if vehicle in self.vehicles:
            self.vehicles.remove(vehicle)

    def get_vehicles(self):
        return self.vehicles

    def get_length(self):
        return self.length
