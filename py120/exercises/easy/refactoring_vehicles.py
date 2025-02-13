class Vehicle:
    def __init__(self, make, model, wheels):
        self.make = make
        self.model = model
        self._wheels = wheels

    @property
    def get_wheels(self):
        return self._wheels

    def info(self):
        return f"{self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model, 4)

class Motorcycle(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model, 2)

class Truck(Vehicle):
    def __init__(self, make, model, payload):
        super().__init__(make, model, 6)
        self.payload = payload

class Boat(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model, 0)

    @property
    def get_wheels(self):
        pass

car1 = Car('Ferrari', 'Fast mobile')
truck1 = Truck('Ford', 'Big Boy', 100)
bike1 = Motorcycle('Ducati', '2 Wheeler')
boat1 = Boat('Supersailor', 'Speeder')
print(bike1.get_wheels)
print(boat1.get_wheels)

print(car1.info())
print(truck1.info())
print(bike1.info())
