class Vehicle:
    def __init__(self, wheels, fuel):
        self.wheels = wheels
        self.fuel =fuel


    def start(self):
        print(f"A {self.wheels} wheeled {self.fuel} vehicle is starting")

    def stop(self):
        print(f"A {self.wheels} wheeled  {self.fuel} vehicle is stopping")


class Car(Vehicle):
    def __init__(self, wheels, fuel, engine):
        super().__init__(wheels, fuel)
        self.engine = engine

    def start(self):
        print(f"A {self.wheels} wheeled {self.engine} {self.fuel} car has started")

maybach = Car("four", "petrol", "V12")
print(maybach.engine)
maybach.start()
maybach.stop()