from abc import ABC, abstractmethod
class Vehical(ABC):
    @abstractmethod
    def display(self):
        pass

class TwoWeeler(Vehical):
    def display(self):
        print("twoweeler")
class FourWeeler(Vehical):
    def display(self):
        print("fourweeler")

class VehicalFactor(ABC):
    @abstractmethod
    def createVehicle(self):
        pass

class TwoWeeherFactory(VehicalFactor):
    def createVehicle(self):
        return TwoWeeler()

class FourWeeherFactory(VehicalFactor):

    def createVehicle(self):
        return FourWeeler()


class Client:

    def __init__(self, vehicalFactory):
        self.vehicalFactory = vehicalFactory.createVehicle()

    def get_vehicle(self):
        return self.vehicalFactory


if __name__ == "__main__":
    print("factory pattern")

    vFactory = TwoWeeherFactory()
    client = Client(vFactory)
    vehicle  = client.get_vehicle()
    vehicle.display()
