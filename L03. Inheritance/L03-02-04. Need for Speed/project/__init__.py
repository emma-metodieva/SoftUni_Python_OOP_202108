# from car import Car
# from cross_motorcycle import CrossMotorcycle
# from family_car import FamilyCar
# from motorcycle import Motorcycle
# from race_motorcycle import RaceMotorcycle
# from sport_car import SportCar
# from vehicle import Vehicle
from project.car import Car
from project.cross_motorcycle import CrossMotorcycle
from project.family_car import FamilyCar
from project.motorcycle import Motorcycle
from project.race_motorcycle import RaceMotorcycle
from project.sport_car import SportCar
from project.vehicle import Vehicle


vehicle = Vehicle(50, 150)
print(Vehicle.DEFAULT_FUEL_CONSUMPTION)
print(vehicle.fuel)
print(vehicle.horse_power)
print(vehicle.fuel_consumption)
vehicle.drive(100)
print(vehicle.fuel)
family_car = FamilyCar(150, 150)
family_car.drive(50)
print(family_car.fuel)
family_car.drive(50)
print(family_car.fuel)
print(family_car.__class__.__bases__[0].__name__)
