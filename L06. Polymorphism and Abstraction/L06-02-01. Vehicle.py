# L06-02. Polymorphism and Abstraction - Exercise
# 01. Vehicle

from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    AC_FUEL_CONSUMPTION = 0.9

    def drive(self, distance):
        trip_fuel_consumption = (self.fuel_consumption + Car.AC_FUEL_CONSUMPTION) * distance
        if trip_fuel_consumption <= self.fuel_quantity:
            self.fuel_quantity -= trip_fuel_consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AC_FUEL_CONSUMPTION = 1.6
    REFUEL_LOSS = 0.05

    def drive(self, distance):
        trip_fuel_consumption = (self.fuel_consumption + Truck.AC_FUEL_CONSUMPTION) * distance
        if trip_fuel_consumption <= self.fuel_quantity:
            self.fuel_quantity -= trip_fuel_consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel * (1 - Truck.REFUEL_LOSS)


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
