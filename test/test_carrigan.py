import unittest
from tires.carrigan import CarriganTire

class TestCarriganTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tire_array = [0.1, 0.5, 0.9, 0.8]
        tire = CarriganTire(tire_array)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        tire_array = [0.1, 0.7, 0.8, 0.8]
        tire = CarriganTire(tire_array)
        self.assertFalse(tire.needs_service())
