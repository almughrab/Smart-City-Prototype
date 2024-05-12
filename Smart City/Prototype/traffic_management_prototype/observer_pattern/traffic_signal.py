from observer_pattern.subject import Subject

class TrafficSignal(Subject):
    def __init__(self):
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update()

    def change_signal(self, signal_state):
        # In a real implementation, this method would change the traffic signal state
        print(f"Traffic signal changed to {signal_state}")
        self.notify_observers()
