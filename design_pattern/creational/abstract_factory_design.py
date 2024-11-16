from abc import ABC, abstractmethod


class Car(ABC):

    @abstractmethod
    def car_type(self):
        pass

class FuelType(ABC):
    @abstractmethod
    def fuel_type(self):
        pass


class Sedan(Car):
    def car_type(self):
        print("Sedan class car")

class HatchBack(Car):
    def car_type(self):
        print("HatchBack class car")

class PetrolCar(FuelType):
    def fuel_type(self):
        print("This is petrol car")

class DieselCar(FuelType):

    def fuel_type(self):
        print("This is diesel car")

class CarFactory(ABC):
    @abstractmethod
    def createCar(self):
        pass

    @abstractmethod
    def createFuelType(self):
        pass

class USACarFactory(CarFactory):

    def createCar(self):
        return Sedan()
    def createFuelType(self):
        return DieselCar()

class EuropeCarFactory(CarFactory):
    def createCar(self):
        return HatchBack()

    def createFuelType(self):
        return PetrolCar()


class Client():

    def __init__(self, car_factory):
        self.car_factory = car_factory

    def create_factory(self):
        car = self.car_factory.createCar()
        fuel_type = self.car_factory.createFuelType()
        car.car_type()
        fuel_type.fuel_type()

if  __name__ == "__main__":

    usaFactory = USACarFactory()
    client = Client(usaFactory)
    client.create_factory()

    print("================")

    europeFactory = EuropeCarFactory()
    client = Client(europeFactory)
    client.create_factory()

    print("=================")



