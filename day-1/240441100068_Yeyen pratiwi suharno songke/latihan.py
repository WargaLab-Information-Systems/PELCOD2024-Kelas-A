nama="Yeyen Pratiwi Suharno Songke"
nim=240441100068
ipk=4.00
mahasiswa=True

print("Nama saya adalah" ,nama)
# ini adalah format narural (tipe data sama)
print("Nim saya adalah",nim)
print("impian ipk saya adalah",ipk) 
print("saya merupakan mahasiswa",mahasiswa)

#ini adalah format string(tipe data di ubah menjadi string)
print(f'nim saya adalah {nim}')

#program dinamis string
nama_panjang=str(input("nama saya adalah :"))

#program dinamis integer
nilai_matematika = int(input("nilai saya adalah :"))

nilai_matematika = 89
nilai_biologi = 75 
nilai_kimia = 90
nilai_fisika = 82

Penjumlahan= nilai_matematika + nilai_kimia
Pengurangan= nilai_matematika - nilai_kimia
perkalian =nilai_matematika * nilai_kimia
pembagian = nilai_matematika / nilai_kimia
print(f'hasil penjumlahan dari matematikandaPenjumlahan= nilai_matematika + nilai_kimian kimia adalah : {Penjumlahan}')

usia_masuk_kuliah=int (input("berapa usia anda saat masuk kuliah?"))
lama_kuliah = int(input ("berapa lama anda kuliah (tahun) ?"))
usia_saat_ini =usia_masuk_kuliah + lama_kuliah
tahun_lulus= 2024 + lama_kuliah

print(f'saya,bernama{nama}saya berusia{usia_masuk_kuliah}')
print(f'saya{nama}akan lulus pada tahun {tahun_lulus}')