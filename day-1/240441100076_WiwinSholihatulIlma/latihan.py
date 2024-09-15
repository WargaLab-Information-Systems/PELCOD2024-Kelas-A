nama = "Wiwin Sholihatul Ilma"
nim = 240441100076
ipk = 4.00
mahasiswa= True

print("Nama saya adalah", nama)
# ini adalah format natural (tipe data sama)
print("Nim saya adalah", nim)
print("Impian Ipk saya adalah", ipk)
print("Saya merupakan Mahasiswa", mahasiswa)

# ini adalah format string (tipe data diubah menjadi string)
print(f'Nama saya adalah {nama}')

# program dinamis string
nama_panjang = str(input("Nama saya adalah : "))

# program dinamis integer
nilai_matematika = int(input("Nilai saya adalah : "))

nilai_matematika = 89
nilai_biologi = 75
nilai_kimia = 90
nilai_fisika = 82

penjumlahan = nilai_matematika + nilai_kimia
pengurangan = nilai_matematika - nilai_kimia
perkalian = nilai_matematika * nilai_kimia
pembagian = nilai_matematika / nilai_kimia

print(f'Hasil dari penjumlahan dari matematika dan kimia adalah : {penjumlahan}')
print(f'Hasil dari pengurangan dari matematika dan kimia adalah : {pengurangan}')
print(f'Hasil dari perkalian dari matematika dan kimia adalah : {perkalian}')
print(f'Hasil dari pembagian dari matematika dan kimia adalah : {pembagian}')

usia_masuk_kuliah = int(input("Berapa usia anda saat masuk kuliah  ?"))
lama_kuliah = int(input("Berapa lama anda kuliah ?"))

usia_saat_ini = usia_masuk_kuliah + lama_kuliah
tahun_lulus = 2022 + lama_kuliah

print(f'Saat ini, saya {nama} berumur {usia_saat_ini}')
print(f'Saya {nama} akan lulus pada tahun {tahun_lulus}')