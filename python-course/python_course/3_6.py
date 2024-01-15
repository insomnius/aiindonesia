# Copyright © 2022 Indonesia AI. All Rights Reserved.
# contact@aiforindonesia.org

# Coba tangkap informasi domisili (Tokyo) dan informasi nomor (021 7581 6521) pada 2 teks berikut
# Gunakan modul regex (re)

import re

teks1 = "Saya yang berdomisili di Tokyo bisa dihubungi di nomor berikut 021 7581 6521"
teks2 = "Nomor ini tidak bisa dihubungi 021 1121 6551, karena sudah di luar area Tokyo"
regexPattern = 'Tokyo|\d+ \d+ \d+'

print(re.findall(regexPattern, teks1))
print(re.findall(regexPattern, teks2))