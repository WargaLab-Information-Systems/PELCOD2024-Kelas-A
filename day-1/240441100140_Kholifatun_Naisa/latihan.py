nama = "Kholifatun Naisa"
nim = 240441100140
ipk = 4.00
mahasiswa = True

print("Nama saya adalah", nama)

#ini adalah format integer
print("Nim saya adalah", nim)

print("Ipk saya adalah", ipk)
print("saya merupakan mahasiswa UTM", mahasiswa)

# ini adalah format string
print(f"nim saya adalah {nim}")

#program dinamis string
nama_panjang = str(input("nama saya adalah : "))

#program dinamis integer
nilai_matematika = int(input("nilai saya adalah : "))

nilai_matematika = 89
nilai_kimia = 75
nilai_biologi = 90
nilai_fisika = 82

penjumlahan = nilai_matematika + nilai_kimia 
perkalian = nilai_matematika * nilai_kimia 
pengurangan = nilai_matematika - nilai_kimia 
pembagian = nilai_matematika / nilai_kimia 

print(f"hasil penjumlahan dari matematika dan kimia: {penjumlahan}")
print(f"hasil perkalian dari matematika dan kimia: {perkalian}")
print(f"hasil perkalian dari matematika dan kimia: {pengurangan}")
print(f"hasil perkalian dari matematika dan kimia: {pembagian}")
      
usia_masuk_kuliah = int (input("berapa usia anda saat masuk kuliah? "))
lama_kuliah = int (input("berapa lama kuliah anda ? "))

usia_saat_ini = usia_masuk_kuliah+lama_kuliah
tahun_lulus = 2024 + lama_kuliah

print(f"saat ini, saya {nama} berumur{usia_saat_ini} ")
print(f"saya {nama} akan lulus pada tahun{tahun_lulus} ")