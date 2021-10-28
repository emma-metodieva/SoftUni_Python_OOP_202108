import unittest
from project.vehicle import Vehicle


class VehicleTest(unittest.TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(30.5, 150)

    def test_vehicle_class_attributes(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_vehicle_init_attributes(self):
        self.assertEqual(30.5, self.vehicle.fuel)
        self.assertEqual(30.5, self.vehicle.capacity)
        self.assertEqual(150, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_vehicle_drive_with_enough_fuel(self):
        self.vehicle.drive(5)
        self.assertEqual(24.25, self.vehicle.fuel)

    def test_vehicle_drive_with_not_enough_fuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(50000)
        self.assertEqual("Not enough fuel", str(ex.exception))
        self.assertEqual(30.5, self.vehicle.fuel)

    def test_vehicle_refuel_within_capacity(self):
        self.vehicle.drive(5)
        self.vehicle.refuel(1)
        self.assertEqual(25.25, self.vehicle.fuel)

    def test_vehicle_refuel_more_than_capacity_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)
        self.assertEqual("Too much fuel", str(ex.exception))
        self.assertEqual(30.5, self.vehicle.fuel)

    def test_vehicle_str(self):
        expected_result = "The vehicle has 150 horse power with 30.5 fuel left and 1.25 fuel consumption"
        self.assertEqual(expected_result, self.vehicle.__str__())


if __name__ == "__main__":
    unittest.main()
