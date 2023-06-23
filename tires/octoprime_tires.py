from tires.tires import Tires


class OctoprimeTires(Tires):
    def __init__(self, tire_wear_sensors):
        self.tire_wear_sensors = tire_wear_sensors

    def needs_service(self):
        return sum(self.tire_wear_sensors) >= 3.0