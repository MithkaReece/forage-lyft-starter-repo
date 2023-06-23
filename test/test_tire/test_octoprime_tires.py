import unittest
from tires.octoprime_tires import OctoprimeTires

class TestCarriganTires(unittest.TestCase):
    def test_needs_service(self):
        tire_wear_sensors = [1, 1, 1, 0.0]

        tires = OctoprimeTires(tire_wear_sensors)
        self.assertTrue(tires.needs_service())

    def test_not_needs_service(self):
        tire_wear_sensors = [0.75, 0.75, 0.75, 0.74]

        tires = OctoprimeTires(tire_wear_sensors)
        self.assertFalse(tires.needs_service())