nama = "RB. Moh Jefri Bassam Azizi Nurcahya"
nim = 240441100144
ipk = 4.00
mahasiswa = True

print("Nama saya adalah", nama)
# ini adalah format natural (tipe data sama)
print("Nim saya adalah", nim)
print("Impian Ipk saya adalah", ipk)
print("Saya merupakan Mahasiswa", mahasiswa)

# ini adalah format string (tipe data diubah menjadi string)
print(f"Nim saya adalah {nim}")

# program dinamis string
nama_panjang = str(input("Nama saya adalah : "))

# program dinamis integer
nilai_matematika = int(input("Nilai saya adalah : "))

# Operator Aritmatika
nilai_matematika = 89
nilai_biologi = 75
nilai_kimia = 90
nilai_fisika = 82

penjumlahan = nilai_matematika + nilai_fisika
pengurangan = nilai_matematika - nilai_fisika
perkalian = nilai_matematika * nilai_fisika
pembagian = nilai_matematika / nilai_fisika

print(f"hasil penjumlahan nilai matematika dan fisika adalah : {penjumlahan}")
print(f"hasil perkalian nilai matematika dan fisika adalah : {perkalian}")

usia_masuk_kuliah = int(input("Berapa usia anda saat masuk kuliah ?"))
lama_kuliah = int(input("Berapa lama anda kuliah ?"))

usia_saat_ini = usia_masuk_kuliah + lama_kuliah
tahun_lulus = 2024 + lama_kuliah

print(f"Saat ini, saya {nama} berumur {usia_saat_ini}")
print(f"saya {nama} akan lulus pada tahun {tahun_lulus}")