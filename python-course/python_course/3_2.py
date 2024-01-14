# Copyright © 2022 Indonesia AI. All Rights Reserved.
# contact@aiforindonesia.org

# Bacalah data yang ada di file data.txt
# Lalu tambahkan teks "Bahasa Pemrograman Python memiliki masa depan yang cerah"
# Pastikan tidak menghilangkan data yang sudah ada di file tersebut!

with open('./python_course/data.txt', mode='r+') as file:
  print("Konten:", file.read())
  file.write("\n\n\nBahasa Pemrograman Python memiliki masa depan yang cerah")

file.close()
