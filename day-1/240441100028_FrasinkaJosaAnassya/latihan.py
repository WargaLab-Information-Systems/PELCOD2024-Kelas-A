nama = "Frasinka Josa Anassya"
nim = 240441100028
ipk = 4.00
mahasiswa = True 

print("nama saya adalah", nama)
#ini adalah format natural (tipe data sama)
print("nim saya adalah", nim)
print("cita cita ipk saya adalah", ipk)
print("saya merupakan mahasiswa adalah", mahasiswa)

#ini adalah format string (tipe dayta diubah menjadi string)
print(f"nama saya adalah {nama}")

#program dinamis int
nama_panjang=str(input("nama saya adalah : "))
#program dinamis int
nilai_matematika=(input("nilai saya adalah :"))

nilai_matematika = 89
nilai_biologi = 75
nilai_kimia = 90
nilai_fisika = 82

penjumlahan = nilai_matematika + nilai_kimia
perkalian = nilai_matematika * nilai_kimia
pengurangan = nilai_matematika - nilai_kimia
pembagian = nilai_matematika / nilai_kimia
print (f"hasil penjumlahan matematika saya dan kimia saya adalah : {penjumlahan}")
print (f"hasil perkalian matematika saya dan kimia saya adalah : {perkalian}")

usia_masuk_kuliah = int(input("berapa usia anda saat masuk kuliah?"))
lama_kuliah = int(input("berapa lama anda kuliah (tahun) ?"))

usia_saat_ini = usia_masuk_kuliah + lama_kuliah
tahun_lulus = 2024 + lama_kuliah

print(f"saat ini, saya  {nama} berumur {usia_saat_ini}")
print(f"saya, bernama {nama} saya akan lulus {tahun_lulus}")
