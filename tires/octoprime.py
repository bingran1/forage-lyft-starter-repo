from re import T
from tires.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, tire_array):
        self.tire_array = tire_array
    
    def needs_service(self):
        sum_value = 0
        for i in self.tire_array:
            sum_value += i
        return True if sum_value >= 3 else False