# L10-01. Unit Testing - Lab
# 04. Car Manager

class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


import unittest


class CarManagerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car('a', 'b', 1, 4)

    def test_car_manager_init_attributes_assignment(self):
        self.assertEqual('a', self.car.make)
        self.assertEqual('b', self.car.model)
        self.assertEqual(1, self.car.fuel_consumption)
        self.assertEqual(4, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_car_manager_make_validation_raises(self):
        new_make = ''
        with self.assertRaises(Exception) as ex:
            self.car.make = new_make
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_car_manager_model_validation_raises(self):
        new_model = ''
        with self.assertRaises(Exception) as ex:
            self.car.model = new_model
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_car_manager_fuel_consumption_validation_raises(self):
        new_fuel_consumptions = [-1, 0]
        for new_fuel_consumption in new_fuel_consumptions:
            with self.assertRaises(Exception) as ex:
                self.car.fuel_consumption = new_fuel_consumption
            self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_car_manager_fuel_capacity_validation_raises(self):
        new_fuel_capacities = [-1, 0]
        for new_fuel_capacity in new_fuel_capacities:
            with self.assertRaises(Exception) as ex:
                self.car.fuel_capacity = new_fuel_capacity
            self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_car_manager_fuel_amount_validation_raises(self):
        new_fuel_amount = -1
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = new_fuel_amount
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_car_manager_refuel_within_capacity(self):
        self.car.refuel(1)
        self.assertEqual(1, self.car.fuel_amount)

    def test_car_manager_refuel_more_than_capacity(self):
        self.car.refuel(5)
        self.assertEqual(4, self.car.fuel_amount)

    def test_car_manager_refuel_negative_amount_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-1)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))
        self.assertEqual(0, self.car.fuel_amount)

    def test_car_manager_drive_enough_fuel(self):
        self.car.refuel(4)
        self.car.drive(2)
        self.assertEqual(3.98, self.car.fuel_amount)

    def test_car_manager_drive_not_enough_fuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(2)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))
        self.assertEqual(0, self.car.fuel_amount)


if __name__ == '__main__':
    unittest.main()
