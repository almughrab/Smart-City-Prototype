class Intersection:
    def __init__(self, name):
        self.name = name
        self.roads = []

    def add_road(self, road):
        self.roads.append(road)

    def get_roads(self):
        return self.roads
