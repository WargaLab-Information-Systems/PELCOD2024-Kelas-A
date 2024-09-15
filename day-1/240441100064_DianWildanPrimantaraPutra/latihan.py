nama = "Dian Wildan Primantara Putra"
nim = 240441100064
ipk = 4.00
mahasiswa = True

# ini adalah format natural (tipe data sama)
print("nama saya adalah", nama)
print("nim saya adalah", nim)
print("impian ipk saya adalah", ipk)
print("saya merupakan mahasiswa", mahasiswa)

# ini adalah format string (tipe data diubah menjadi string)
print(f"nim saya adalah {nim}")

# proram dinamis string
nama_panjang= str(input("nama saya adalah : "))

# Program dinamis integer
nilai_matematika= int(input("nilai matematika saya adalah : "))

# Operator Aritmatika
nilai_matematika = 89
nilai_biologi = 75
nilai_kimia = 90
nilai_fisika = 82

penjumlahan = nilai_matematika + nilai_kimia
pengurangan = nilai_matematika - nilai_kimia
pembagian = nilai_matematika / nilai_kimia
perkalian = nilai_matematika * nilai_kimia

print(f"Hasil penjumlahan nilai matematika dan nilai kimia adalah : {penjumlahan}")
print(f"Hasil pengurangan nilai matematika dan nilai kimia adalah : {pengurangan}")
print(f"Hasil pembagian nilai matematika dan nilai kimia adalah : {pembagian}")
print(f"Hasil perkalian nilai matematika dan nilai kimia adalah : {perkalian}")

usia_masuk_kuliah = int (input("berapa usia anda saat masuk kuliah ?"))
lama_kuliah = int (input("berapa lama anda kuliah (tahun) ?"))

usia_saat_ini = usia_masuk_kuliah + lama_kuliah
tahun_lulus = 2024 + lama_kuliah

print(f"saat ini, saya {nama} saya berumur {usia_saat_ini}")
print(f"saya, {nama} akan lulus pada tahun {tahun_lulus}")