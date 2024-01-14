# Copyright © 2022 Indonesia AI. All Rights Reserved.
# contact@aiforindonesia.org

# Buatlah operasi loop yang akan mencetak angka GENAP dari 1-120
# Lalu gunakan statement continue agar operasi tidak mencetak angka 12, 56 dan 78
# Dan juga gunakan statement break agar operasi berhenti hanya sampai di angka 100

list_angka = range(1, 120)
print("list angka:", list_angka)

for angka in list_angka:
  if angka in [12, 56, 78]:
    continue

  if angka%2 == 0:
    print(angka)

  if angka == 100:
    break
