nama = "Hilyatul Abidah"
nim = 240441100132
ipk = 3.80
mahasiswa = True

print("nama saya adalah", nama)
# ini adalah format natural (tipe data sama)
print("nim saya adalah", nim)
print("impian ipk saya adalah", ipk)
print("saya merupakan mahasiswa", mahasiswa)

# ini adalah format string (tipe data diubah menjadi string)
print(f"nim saya adalah {nim}")

# program dinamis string
nama_panjang = str(input("nama saya adalah : "))

# program dinamis integer
nilai_matematika = int(input ("nilai saya adalah : "))

nilai_matematika = 89
nilai_biologi = 75
nilai_kimia = 90
nilai_fisika = 82

penjumlahan = nilai_matematika + nilai_kimia
pengurangan= nilai_matematika - nilai_kimia
perkalian= nilai_matematika * nilai_kimia
pembagian= nilai_matematika / nilai_kimia

print(f"hasil penjumlahan dari matematika dan kimia adalah : {penjumlahan}")
print(f"hasil pengurangan dari matematika dan kimia adalah : {pengurangan}")
print(f"hasil perkalian dari matematika dan kimia adalah : {perkalian}")
print(f"hasil pembagian dari matematika dan kimia adalah : {pembagian}")

usia_masuk_kuliah = int(input("berapa usia anda ?"))
lama_kuliah = int(input("berapa lama anda kuliah (tahun) ?"))

usia_saat_ini = usia_masuk_kuliah + lama_kuliah
tahun_lulus = 2022 + lama_kuliah

print(f"saat ini, saya {nama} berusia {usia_masuk_kuliah} ")
print(f"saya {nama} saya akan lulus pada tahun {tahun_lulus} ")