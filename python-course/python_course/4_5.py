# Copyright © 2022 Indonesia AI. All Rights Reserved.
# contact@aiforindonesia.org

# Setelah class mobil, buatlah satu class baru bernama motor
# Terapkan konsep Polimorphism yang sudah dipelajari dengan membuat satu fungsi umum bernama menampung()


class Mobil:
    def __init__(self, brand='Toyota', model='Innova'):
        self.brand = brand
        self.model = model

    def menampung(self):
        print(f"{self.brand} {self.model} dapat menampung 5 penumpang.")

class Motor:
    def __init__(self, brand='Honda', model='Supra'):
        self.brand = brand
        self.model = model

    def menampung(self):
        print(f"{self.brand} {self.model} dapat menampung 2 penumpang.")

def menampung(objek):
    objek.menampung()

# Contoh penggunaan polimorfisme
mobil_saya = Mobil()
motor_saya = Motor()

menampung(mobil_saya)  # Memanggil metode menampung() pada objek Mobil
menampung(motor_saya)  # Memanggil metode menampung() pada objek Motor
