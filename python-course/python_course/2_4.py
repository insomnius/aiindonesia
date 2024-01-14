# Copyright © 2022 Indonesia AI. All Rights Reserved.
# contact@aiforindonesia.org

# Buatlah satu logika kondisi yang menentukan jika harga laptop sekian maka
# saya akan mempertimbangkan lagi jika harga handphone sekian maka saya akan beli keduanya atau tidak
# Gunakan teknik NESTED IF!

harga_laptop = 100
harga_handphone = 50
if harga_laptop <= 100:
  if harga_handphone <= 50:
      print("Saya akan beli handphone dan hape.")
      exit(0)
  print("Saya akan beli laptop aja.")
