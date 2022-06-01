from re import T
import unittest
from datetime import datetime
from battery.spinder import Spinder

class TestSpinderBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        battery = Spinder(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        battery = Spinder(last_service_date, today)
        self.assertFalse(battery.needs_service())
