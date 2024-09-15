nama = "Febrianti Nur Anggraini"
NIM = 240441100024
ipk = 4.00
mahasiswa = True

print("nama saya adalah febby", nama)
# ini adalah format natural (tipe data sama)
print("NIM saya adalah", NIM) 
print("cita cita ipk saya adalah 4.00", ipk)
print("saya merupakan mahasiswa ", mahasiswa)

# ini adalah format string (tipe data diubah menjadi string)
print(f"NIM saya adalah {NIM}")

#program dinamis integer
nama_panjang = str (input ("nama saya adalah :"))

#program dinamis integer 
nilai_matematika = int (input("nilai saya adalah;"))

nilai_matematika = 89
nilai_biologi = 75
nilai_kimia = 90
nilai_fisika = 82

penjumlahan = nilai_matematika + nilai_kimia
perkalian = nilai_matematika * nilai_kimia
pengurangan = nilai_matematika - nilai_kimia
pembagian = nilai_matematika / nilai_kimia

print(f" hasil penjumlahan nilai fisika dan kimia adalah: {penjumlahan}")
print(f" hasil pengurangan nilai matematika dan kimia adalah: {pengurangan}" )
print(f" hasil perkalian nilai matematika dan kimia adalah: {perkalian}" )
print(f" hasil pembagian nilai matematika dan kimia adalah: {pembagian}" )

usia_masuk_kuliah = int(input ("berapa usia anda?"))
lama_kuliah = int (input ("berapa lama kulian (tahun) ?"))

usia_saat_ini = usia_masuk_kuliah + lama_kuliah
tahun_lulus = 2024 + lama_kuliah

print(f'saat ini,saya {nama} berumur {usia_saat_ini}')
print(f'saya {nama} akan lulus pada tahun {tahun_lulus}')