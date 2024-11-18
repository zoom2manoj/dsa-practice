


class Singleton(type):

    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            instance = super().__call__(*args, **kwargs)
            cls._instance[cls] = instance


class SingleDemo(metaclass=Singleton):

    def __init__(self, *args, **kwargs):
        print("hi")


a = SingleDemo()
b = SingleDemo()
print(f"a id: {id(a)}\nb id: {id(b)}")