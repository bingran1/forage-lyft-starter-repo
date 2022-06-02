from re import T
from tires.tire import Tire

class CarriganTire(Tire):
    def __init__(self, tire_array):
        self.tire_array = tire_array

    def needs_service(self):
        for each in self.tire_array:
            if each >= 0.9:
                return True
        return False

