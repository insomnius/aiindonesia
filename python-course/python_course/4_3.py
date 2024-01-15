# Copyright © 2022 Indonesia AI. All Rights Reserved.
# contact@aiforindonesia.org

# Kembangkanlah class Mobil yang sudah dibuat sebelumnya agar memiliki fungsi setter & getter
# Pastikan fungsi tersebut memungkinkan kita untuk memodifikasi semua attributes yang dimiliki oleh class tersebut

class Mobil:
    def __init__(self, brand='Toyota', model='Innova', transmission='Automatic'):
        self._brand = brand
        self._model = model
        self._transmission = transmission
        self._is_engine_on = False
        self._speed = 0

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, new_brand):
        self._brand = new_brand

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, new_model):
        self._model = new_model

    @property
    def transmission(self):
        return self._transmission

    @transmission.setter
    def transmission(self, new_transmission):
        self._transmission = new_transmission

    @property
    def is_engine_on(self):
        return self._is_engine_on

    @property
    def speed(self):
        return self._speed

    def start_engine(self):
        if not self._is_engine_on:
            print(f"Starting the engine of {self._brand} {self._model}.")
            self._is_engine_on = True
        else:
            print(f"The engine of {self._brand} {self._model} is already running.")

    def drive(self, speed):
        if self._is_engine_on:
            print(f"{self._brand} {self._model} is moving at {speed} km/h.")
            self._speed = speed
        else:
            print(f"Start the engine first to drive {self._brand} {self._model}.")

    def stop(self):
        if self._is_engine_on and self._speed > 0:
            print(f"{self._brand} {self._model} is coming to a stop.")
            self._speed = 0
        elif not self._is_engine_on:
            print(f"The engine of {self._brand} {self._model} is not running.")
        else:
            print(f"{self._brand} {self._model} is already stationary.")

# Contoh penggunaan class Mobil dengan setter & getter
my_car = Mobil()

# Menggunakan setter
my_car.brand = 'Honda'
my_car.model = 'Civic'
my_car.transmission = 'Manual'

# Menggunakan getter
print(f"Brand: {my_car.brand}")
print(f"Model: {my_car.model}")
print(f"Transmission: {my_car.transmission}")

my_car.start_engine()
my_car.drive(60)
my_car.stop()
