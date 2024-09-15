nama = "miftakhul arinda"
nim = 240441100100
ipk = 4.00
mahasiswa = True 

print("Nama saya adalah", nama)
# ini adalah format natural (tipe data sama)
print("Nim saya adalah", nim)
print("Impian Ipk saya adalah", ipk)
print("Saya merupakan mahasiswa", mahasiswa)

# ini adalah format string (tipe data iubah menjadi string)
print(f'Nim saya adalah {nim}')

# program dinamis string
nama_panjang = str(input("Nama saya adalah : "))

# program dinamis integer
nilai_matematika = int(input("Nilai saya adalah : "))

nilai_matematika = 89
nilai_biologi = 75
nilai_kimia = 90
nilai_fisika = 81

penjumlahan = nilai_matematika + nilai_kimia
pengurangan = nilai_matematika - nilai_kimia
perkalian = nilai_matematika * nilai_kimia
pembagian = nilai_matematika / nilai_kimia

print(f'hasil penjumlahan dari matematika dan kimia adalah : {penjumlahan}')
print(f'hasil pengurangan dari matematika dan kimia adalah : {pengurangan}')
print(f'hasil perkalian dari matematika dan kimia adalah : {perkalian}')
print(f'hasil pembagian dari matematika dan kimia adalah : {pembagian}')

usia_masuk_kuliah = int(input("berapa usia anda saat masuk kuliah ?"))
lama_kuliah = int(input("berapa lama anda kuliah (tahun) ?"))

usia_saat_ini = usia_masuk_kuliah + lama_kuliah
tahun_lulus = 2024 + lama_kuliah

print(f'Saat ini, saya {nama} berumur {usia_saat_ini}')
print(f'Saya {nama} akan lulus pada tahun {tahun_lulus}')