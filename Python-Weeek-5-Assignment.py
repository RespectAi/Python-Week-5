# Assignment 1: Design Your Class

class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def send_message(self, number, message):
        print(f"Sending message from {self.brand} {self.model} to {number}: {message}")

    def display_info(self):
        print(f"Smartphone Info:")
        print(f"  Brand: {self.brand}")
        print(f"  Model: {self.model}")
        print(f"  Price: ${self.price}")

# Inheritance: A subclass with additional feature(s)
class SmartphonePro(Smartphone):
    def __init__(self, brand, model, price, camera_megapixels):
        super().__init__(brand, model, price)  # Initialize parent class attributes.
        self.camera_megapixels = camera_megapixels

    # Overriding display_info to include the camera information.
    def display_info(self):
        super().display_info()
        print(f"  Camera: {self.camera_megapixels} Megapixels")

# Testing Assignment 1
print("Assignment 1: Custom Class")
basic_phone = Smartphone("TechCo", "X100", 299)
basic_phone.display_info()
basic_phone.call("123-456-7890")
basic_phone.send_message("123-456-7890", "Hello, this is a test message!")

print("\n--- Enhanced Version ---")
pro_phone = SmartphonePro("TechCo", "XPro", 499, 48)
pro_phone.display_info()


# Assignment 2

# Base class for all vehicles. This method expects to be overridden.
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")

# Subclass representing a Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Subclass representing a Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Subclass representing a Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")

# Testing polymorphism by calling move() on each vehicle object.
print("\nAssignment 2")
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()  # Each vehicle prints its specific move action.
# Assignment 2: Polymorphism Challenge

# Base class for all vehicles. This method expects to be overridden.
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")

# Subclass representing a Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Subclass representing a Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Subclass representing a Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")

# Testing polymorphism by calling move() on each vehicle object.
print("\nAssignment 2")
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()  # Each vehicle prints its specific move action.
