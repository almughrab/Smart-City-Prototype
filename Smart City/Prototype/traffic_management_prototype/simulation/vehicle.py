class Vehicle:
    def __init__(self, id, road, speed):
        self.id = id
        self.road = road
        self.position = 0  # Current position on the road
        self.speed = speed

    def move(self):
        self.position += self.speed

    def get_position(self):
        return self.position

    def get_road(self):
        return self.road
