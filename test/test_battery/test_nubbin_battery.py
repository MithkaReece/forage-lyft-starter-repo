import unittest
from battery.nubbin_battery import NubbinBattery
from datetime import datetime

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 4)

        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_not_needs_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)

        battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())