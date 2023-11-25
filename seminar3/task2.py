# Переписать код SpeedCalculation в соответствии с Open-Closed Principle:

class Vehicle:
    def __init__(self, max_speed, vehicle_type):
        self.max_speed = max_speed
        self.vehicle_type = vehicle_type

    def get_max_speed(self):
        return self.max_speed

    def get_type(self):
        return self.vehicle_type


class Car(Vehicle):
    def calculate_allowed_speed(self):
        return self.get_max_speed() * 0.8


class Bus(Vehicle):
    def calculate_allowed_speed(self):
        return self.get_max_speed() * 0.6


class SpeedCalculation:
    def calculate_allowed_speed(self, vehicle):
        if isinstance(vehicle, Vehicle):
            return vehicle.calculate_allowed_speed()
        return 0.0
