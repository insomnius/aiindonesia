# Copyright © 2022 Indonesia AI. All Rights Reserved.
# contact@aiforindonesia.org

# Buatlah satu class Mobil yang bisa digunakan untuk mencetak beragam tipe mobil
# Pastikan class tersebut memiliki setidaknya 3 attributes dan 3 methods

class Mobil:
    def __init__(self, brand='Toyota', model='Innova', transmission='Automatic'):
        self.brand = brand
        self.model = model
        self.transmission = transmission
        self.is_engine_on = False
        self.speed = 0

    def start_engine(self):
        if not self.is_engine_on:
            print(f"Starting the engine of {self.brand} {self.model}.")
            self.is_engine_on = True
        else:
            print(f"The engine of {self.brand} {self.model} is already running.")

    def drive(self, speed):
        if self.is_engine_on:
            print(f"{self.brand} {self.model} is moving at {speed} km/h.")
            self.speed = speed
        else:
            print(f"Start the engine first to drive {self.brand} {self.model}.")

    def stop(self):
        if self.is_engine_on and self.speed > 0:
            print(f"{self.brand} {self.model} is coming to a stop.")
            self.speed = 0
        elif not self.is_engine_on:
            print(f"The engine of {self.brand} {self.model} is not running.")
        else:
            print(f"{self.brand} {self.model} is already stationary.")

# Contoh penggunaan class Mobil
my_car = Mobil(brand='Honda', model='Civic', transmission='Manual')

my_car.start_engine()
my_car.drive(60)
my_car.stop()

my_car.start_engine()
my_car.drive(80)
my_car.stop()

my_car.start_engine()
my_car.drive(100)
my_car.stop()
