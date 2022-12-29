import object_factory

from pprint import pprint

class Car:
    def __init__(self, type: str, specs=None):
        print(f"Car::__init__(type={type}, specs={specs})")
        self.m_type = type
        self.m_ac = specs['A/C']
        self.m_transmission = specs['transmission']

class Toyota(Car):
    def __init__(self, specs=None):
        super(Toyota, self).__init__('Toyota', specs)
        print(f"Toyota::__init__(specs={specs})")
        self.m_onstar = specs['on-star']

class Honda(Car):
    def __init__(self, specs=None):
        super(Honda, self).__init__('Honda', specs)
        print(f"Honda::__init__(specs={specs})")
        self.m_warranty = specs['warranty']

def create_honda(specs):
    print(f"create_honda(specs={specs})")
    return Honda(specs)

def main():
    carFactory = object_factory.ObjectFactory()
    carFactory.register('Toyota', Toyota)
    #carFactory.register('Honda', Honda)
    carFactory.register('Honda', create_honda)

    carSpecs = [
        {
            "type": "Toyota",
            "A/C": True,
            "transmission": "manual",
            "on-star": False
        },
        {
            "type": "Honda",
            "A/C": True,
            "transmission": "automatic",
            "warranty": "extended"
        }
    ]

    for specs in carSpecs:
        print(f"specs={specs}")
        car = carFactory.create(specs['type'], specs=specs)

        pprint(vars(car))

if __name__ == '__main__':
    main()
