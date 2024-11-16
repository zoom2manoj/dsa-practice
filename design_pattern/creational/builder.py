from abc import ABC, abstractmethod


class Computer():

    def __init__(self, cpu=None, ram=None, storage=None):
        self.ram = ram
        self.cpu = cpu
        self.storage = storage

    def show(self):
        print(f"computer is having {self.ram} ram, {self.cpu} cpu type and {self.storage} storage")


class Builder(ABC):
    @abstractmethod
    def get_ram(self):
        pass

    @abstractmethod
    def get_cpu(self):
        pass

    @abstractmethod
    def get_storage(self):
        pass

class BuilderCreation(Builder):

    def __init__(self):
        self.computer = Computer()

    def get_cpu(self):
        self.computer.cpu = "Intel"
    def get_ram(self):
        self.computer.ram = "32GB"

    def get_storage(self):
        self.computer.storage = "60T"

    def information(self):
        return self.computer


class Director:

    def __init__(self, builder):
        self.builder = builder


    def construct(self):
        self.builder.get_cpu()
        self.builder.get_ram()
        self.builder.get_storage()


if __name__ == "__main__":

    builder = BuilderCreation()
    director = Director(builder)
    director.construct()
    computer = builder.information()
    computer.show()





