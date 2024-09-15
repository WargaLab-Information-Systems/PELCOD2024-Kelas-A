nama = "Arya Surya NUgraha"
nim = 240441100148
ipk = 4.00
mahasiswa = True

print("nama saya adalah", nama)
# ini adalah format natural (tipe data sama)
print("nim saya adalah", nim)
print("impian ipk saya adalah", ipk)
print("saya merupakan mahasiswa", mahasiswa)

#ini adalah format string (tipe data diubah menjadi string)
print(f"nama saya adalah {nama}")

# program dinamis string 
nama_panjang = str(input("nama saya adalah"))

# program dinamis integer
nilai_matematika = int(input("nilai saya adalah :"))

nilai_matematika = 89
nilai_biologi = 75
nilai_kimia = 90
nilai_fisika = 82

penjumlahan = nilai_matematika + nilai_kimia 
pengurangan = nilai_matematika - nilai_kimia
perkalian = nilai_matematika * nilai_kimia 
pembagian = nilai_matematika / nilai_kimia 

print(f"hasil penjumlahan dari matematika dan kimia adalah :{penjumlahan}")
print(f"hasil penjumlahan dari matematika dan kimia adalah :{penjumlahan}")

usia_masuk_kuliah = int(input("berapa usia anda ?"))
lama_kuliah = int(input("berapa lama anda kuliah (tahun) ?"))

usia_saat_ini = usia_masuk_kuliah + lama_kuliah 
tahun_lulus = 2022 + lama_kuliah 

print(f'saat ini, saya {nama} berumur {usia_saat_ini}')
print(f'saya {nama} akan lulus pada tahun {tahun_lulus}')