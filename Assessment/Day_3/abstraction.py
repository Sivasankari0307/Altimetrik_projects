# Example for abstraction

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def fuel_type(self):
        pass

class Bike(Vehicle):
    def fuel_type(self):
        print("Bike uses petrol")
    def own_method(self):
        print("Bike uses petrol")

class electricBike(Vehicle):
    def fuel_type(self):
        print("Electric bike uses battery")


b = Bike()
e = electricBike()

b.fuel_type()
e.fuel_type()
b.own_method()