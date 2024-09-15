nama ="Moh Hilmiy Fuadi"
nim = 240441100156
ipk = 4.00
mahasiswa = True

#ini adalah format natural (tipe data sama)
print("nama saya adalah", nama)
print("nim saya adalah", nim)
print("impian ipk saya adalah", ipk)
print("saya merupakan mahasiswa", mahasiswa)

# ini adalah format string(tipe data diubah menjadi string)
print(f"Nim saya adalah{nim}")

# program dinamis string
nama_panjang = str(input("Nama saya adalah : "))

# program dinamis integer
nilai_matematika = int(input("nilai saya adalah  : "))

nilai_matematika = 89
nilai_biologi = 75
nilai_kimia = 90
nilai_fisika = 82

penjumlahan = nilai_matematika + nilai_biologi
pengurangan = nilai_biologi - nilai_fisika
perkalian = nilai_fisika * nilai_kimia
pembagian = nilai_matematika / nilai_fisika

print (f'Hasil penjumlahan dari matematika dan biologi adalah : {penjumlahan} ') 
print (f'Hasil penjumlahan dari biologi dan fisika adalah : {pengurangan} ') 
print (f'Hasil penjumlahan dari fisika dan kimia adalah : {perkalian} ') 
print (f'Hasil penjumlahan dari matematika dan fisika adalah : {pembagian} ') 

usia_masuk_kualiah = int(input("berapa usia anda saat masuk kuliah?"))
lama_kualiah = int(input("berapa lama  anda kuliah (tahun) ?"))

usia_saat_ini = usia_masuk_kualiah + lama_kualiah
tahun_lulus = 2022 + lama_kualiah

print(f'saat ini, saya {nama} berumur {usia_saat_ini}')
print(f'saya, {nama} akan lulus pada tahun {tahun_lulus}')