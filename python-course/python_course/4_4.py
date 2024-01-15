# Copyright © 2022 Indonesia AI. All Rights Reserved.
# contact@aiforindonesia.org

# Kembangkanlah class Mobil yang sudah dibuat sebelumnya agar memiliki parent class bernama Kendaraan
# Pastikan parent class tersebut memiliki setidaknya 2 attributes dan 2 methods yang akan diturunkan ke child class
# Jangan lupa menggunakan super() pada child class

# Parent class
class Kendaraan:

    def __init__(self, warna='Hitam', roda=4):
        self.warna = warna
        self.roda = roda

    def info(self):
        print(f"Kendaraan berwarna {self.warna} dan memiliki {self.roda} roda.")

    def klakson(self):
        print("Tin tin!")

# Child class
class Mobil(Kendaraan):
    def __init__(self, brand='Toyota', model='Innova', transmission='Automatic'):
        super().__init__()
        self.brand = brand
        self.model = model
        self.warna = 'putih'
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

# Contoh penggunaan class Mobil sebagai child class dari Kendaraan
my_car = Mobil()

# Memanggil metode dari parent class
my_car.info()
my_car.klakson()

# Memanggil metode dari child class
my_car.start_engine()
my_car.drive(60)
my_car.stop()
