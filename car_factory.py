from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery


class CarFactory():
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_sensors):
        return Car(
            CapuletEngine(last_service_mileage, current_mileage),
            SpindlerBattery(last_service_date, current_date),
        )
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_sensors):
        return Car(
            WilloughbyEngine(last_service_mileage, current_mileage),
            SpindlerBattery(last_service_date, current_date),
        )
    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on, tire_wear_sensors):
        return Car(
            SternmanEngine(warning_light_on),
            SpindlerBattery(last_service_date, current_date),
        )
    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_sensors):
        return Car(
            WilloughbyEngine(last_service_mileage, current_mileage),
            NubbinBattery(last_service_date, current_date),
        )
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_sensors):
        return Car(
            CapuletEngine(last_service_mileage, current_mileage),
            NubbinBattery(last_service_date, current_date),
       )