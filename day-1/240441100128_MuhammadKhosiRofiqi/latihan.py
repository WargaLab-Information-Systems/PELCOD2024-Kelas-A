nama = "muhammad khosi rofiqi"
nim = 210441100128
ipk = 4.00
mahasiswa = True

# ini adalah format natural (tipe data sama)
print("Nama saya adalah", nama)
# ini adalah format natural (tipe data sama)
print("Nim saya adalah", nim)
print("Impian ipk saya adalah", ipk)
print("Saya merupakan mahasiswa", mahasiswa)

# ini adalah format string (tipe data di ubah menjadi)
print(f'Nim saya adalah {nim}')

#program dinamis string
nama_panjang = str(input("Nama saya adalah : "))

#program dinamis integer
nilai_matematika = str(input("Nilai saya adalah : "))


nilai_matematika = 89
nilai_biologi = 75
nilai_kimia = 90
nilai_fisika = 82

penjumlahan = nilai_matematika + nilai_kimia
perkalian = nilai_matematika * nilai_kimia
perkalian = nilai_matematika - nilai_kimia
perkalian = nilai_matematika / nilai_kimia

print(f'hasil penjumlahan dari matematika dan kimia adalah {penjumlahan}')
print(f'hasil perkalian dari matematika dan kimia adalah {perkalian}')

usia_masuk_kuliah = int(input("berapa usia anda?"))
lama_kuliah = int(input("berapa lama anda kuliah (tahun) ?"))

usia_saat_ini = usia_masuk_kuliah + lama_kuliah
tahun_lulus = 2027 + lama_kuliah

print (f'saya, bernama {nama} saya berusia {usia_saat_ini}')
print (f'saya, {nama} akan lulus pada tahun {tahun_lulus}')