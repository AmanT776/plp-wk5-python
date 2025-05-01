class Vehicle:
    def __init__(self,color,model):
        self.color = color
        self.model = model
    def move(self):
        print("This vehicle moves in a generic way.")
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")
class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()
