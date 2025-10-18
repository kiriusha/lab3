class Transport:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def move(self):
        print(f"Transport is moving at {self.speed} km/h")

    def __str__(self):
        return f"Transport: {self.brand}, Speed: {self.speed}"

    def __len__(self):
        return self.seats

    def __eq__(self, other):
        if isinstance(other, Car):
            return self.speed == other.speed
        return False

    def __add__(self, other):
        if isinstance(other, Car):
            return self.speed + other.speed
        return NotImplemented


class Car(Transport):
    def __init__(self, brand, speed, seats):
        super().__init__(brand, speed)
        self.seats = seats

    def honk(self):
        print("Бип-бип!")

    def move(self):
        print(f"Car {self.brand} is driving at {self.speed} km/h")

    def __str__(self):
        return f"Transport: {self.brand}, Speed: {self.speed}, Seats: {self.seats}"


class Bike(Transport):
    def __init__(self, brand, speed, bike_type):
        super().__init__(brand, speed)
        self.type = bike_type

    def move(self):
        print(f"Bike {self.brand} is cycling at {self.speed} km/h")

    def __str__(self):
        return f"Transport: {self.brand}, Speed: {self.speed}, Type: {self.type}"



# Задание 1
t = Transport("Toyota", 120)
print(t)
t.move()

# Задание 2
car = Car("Toyota", 120, 5)
bike = Bike("Giant", 25, "горный")

print(car)
car.move()
car.honk()

print("\n" + str(bike))
bike.move()

# Задание 3
car1 = Car("Toyota", 120, 5)
car2 = Car("Honda", 150, 4)

print(f"Количество мест в car1: {len(car1)}")
print(f"car1 и car2 одинаковой скорости: {car1 == car2}")
print(f"Суммарная скорость: {car1 + car2} км/ч")

#Задание 4
car = Car("Toyota", 120, 5)
bike = Bike("Giant", 25, "горный")

try:
    result = car + bike
except TypeError as e:
    print(f"Метод add не определён для класса bike")

# Задание 5
transports = [
    Transport("Грузовик", 80),
    Car("Toyota", 120, 5),
    Bike("Giant", 25, "горный")
]

print("Демонстрация полиморфизма:")
for transport in transports:
    transport.move()