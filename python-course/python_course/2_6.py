# Copyright © 2022 Indonesia AI. All Rights Reserved.
# contact@aiforindonesia.org

# Buatlah fungsi yang akan mengevaluasi apakah modulus dari hasil kali 2 angka yang diterima bernilai 0 atau tidak
# Gunakan statement return untuk mengembalikan nilai tersebut lalu cetak hasilnya
# Beri nama cek_modulus() pada fungsi tersebut

angka1 = 12
angka2 = 8

def cek_modulus(x, y):
  return x%y == 0

print(cek_modulus(angka1, angka2))