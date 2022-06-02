import unittest
from tires.octoprime import OctoprimeTire

class TestOctoprimeTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tire_array = [0.9, 0.5, 0.9, 0.8]
        tire = OctoprimeTire(tire_array)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        tire_array = [0.1, 0.2, 0.3, 0.4]
        tire = OctoprimeTire(tire_array)
        self.assertFalse(tire.needs_service())
