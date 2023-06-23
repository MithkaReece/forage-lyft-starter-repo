import unittest
from tires.carrigan_tires import CarriganTires

class TestCarriganTires(unittest.TestCase):
    def test_needs_service(self):
        tire_wear_sensors = [0.9, 0.0, 0.0, 0.0]

        tires = CarriganTires(tire_wear_sensors)
        self.assertTrue(tires.needs_service())

    def test_not_needs_service(self):
        tire_wear_sensors = [0.89, 0.89, 0.89, 0.89]

        tires = CarriganTires(tire_wear_sensors)
        self.assertFalse(tires.needs_service())