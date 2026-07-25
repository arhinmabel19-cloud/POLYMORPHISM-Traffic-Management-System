# Parent Class
class TrafficDevice:
    def activate(self):
        raise NotImplementedError("Subclasses must override this method")


# Child Classes
class TrafficLight(TrafficDevice):
    def activate(self):
        print("Traffic Light: Changing signals (Red → Green → Yellow)")


class SpeedCamera(TrafficDevice):
    def activate(self):
        print("Speed Camera: Capturing speed violations")


class PedestrianSignal(TrafficDevice):
    def activate(self):
        print("Pedestrian Signal: Allowing pedestrians to cross")


# New Class (Added without modifying activation loop)
class EmergencySiren(TrafficDevice):
    def activate(self):
        print("Emergency Siren: Clearing traffic for emergency vehicle")


# Create objects and store in a list
devices = [
    TrafficLight(),
    SpeedCamera(),
    PedestrianSignal(),
    EmergencySiren()  # Added seamlessly
]

# Activate all devices (Polymorphism in action)
for device in devices:
    device.activate()