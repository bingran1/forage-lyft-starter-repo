from car import *
from engine.capulet_engine import *
from engine.sternman_engine import *
from engine.willoughby_engine import *
from battery.nubbin import *
from battery.spinder import *
from tires.carrigan import *
from tires.octoprime import *

class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_array):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = Spinder(last_service_date, current_date)
        tire = CarriganTire(tire_array)
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_array):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = Spinder(last_service_date, current_date)
        tire = OctoprimeTire(tire_array)
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on, tire_array):
        engine = SternmanEngine(warning_light_is_on)
        battery = Spinder(last_service_date, current_date)
        tire = CarriganTire(tire_array)
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_array):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = Nubbin(last_service_date, current_date)
        tire = OctoprimeTire(tire_array)
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_array):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = Nubbin(last_service_date, current_date)
        tire = CarriganTire(tire_array)
        car = Car(engine, battery, tire)
        return car


