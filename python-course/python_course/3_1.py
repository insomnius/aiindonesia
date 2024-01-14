# Copyright © 2022 Indonesia AI. All Rights Reserved.
# contact@aiforindonesia.org

# Buatlah 2 buah dictionary yang memuat informasi 10 murid dan informasi 10 karyawan
# Lalu cetak data murid dan karyawan yang berada di-index 2 dan 9
# Setelah itu cetak semua data yang ada di dictionary tersebut dengan for loop

dict_murid = {
    1: {'nama': 'Murid1', 'kelas': 'XII A'},
    2: {'nama': 'Murid2', 'kelas': 'XI B'},
    3: {'nama': 'Murid3', 'kelas': 'X A'},
    4: {'nama': 'Murid4', 'kelas': 'XII C'},
    5: {'nama': 'Murid5', 'kelas': 'XI A'},
    6: {'nama': 'Murid6', 'kelas': 'XII B'},
    7: {'nama': 'Murid7', 'kelas': 'XI C'},
    8: {'nama': 'Murid8', 'kelas': 'X B'},
    9: {'nama': 'Murid9', 'kelas': 'XI A'},
    10: {'nama': 'Murid10', 'kelas': 'XII A'}
}

dict_karyawan = {
    1: {'nama': 'Karyawan1', 'posisi': 'Manajer'},
    2: {'nama': 'Karyawan2', 'posisi': 'Staf'},
    3: {'nama': 'Karyawan3', 'posisi': 'Asisten Manajer'},
    4: {'nama': 'Karyawan4', 'posisi': 'Staf'},
    5: {'nama': 'Karyawan5', 'posisi': 'Manajer'},
    6: {'nama': 'Karyawan6', 'posisi': 'Staf'},
    7: {'nama': 'Karyawan7', 'posisi': 'Manajer'},
    8: {'nama': 'Karyawan8', 'posisi': 'Asisten Manajer'},
    9: {'nama': 'Karyawan9', 'posisi': 'Staf'},
    10: {'nama': 'Karyawan10', 'posisi': 'Manajer'}
}

print("Data Murid di Index 2:", dict_murid[2])
print("Data Karyawan di Index 9:", dict_karyawan[9])