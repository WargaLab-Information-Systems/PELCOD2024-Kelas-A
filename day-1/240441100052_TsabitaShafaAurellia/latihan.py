nama="tsabita"
nim=240441100052
ipk=4.00
mahasiswa=True

#print(,"nama saya adalah",nama)
# ini adalah format natural (tipe data sama)
# print(,"nim saya adalah",nama)
# print(,'cita cita ipk saya adalah',ipk)
# print(,'mahasiswa saya adalah',mahasiswa
#print(,'mahasiswa saya adalah'nama)
#ini adalah format string(tipe data diubah menjadi)
print(f"nim saya adalah{nim}")
#program dinamis string
nama_panjang= str(input("nama saya adalah"))
#program dinamis string
nilai_matematika = int (input("perkenlkan nama saya:", nama))
# nilai_biologi= 89
# nilai_matematika= 75
# nilai_kimia = 90
# nilai_fisika = 82

# print(f"")
# penjumlahan= nilai_matematika + nilai_ kimia
# perkalian= nilai_matematika* nilai_kimia
# print(f"hasil penjumlahan dari matematikadan kimia : {penjumlahan}"
# print(f"hasil penjumlahan dari matematika dan kimia : {perkalian}")

usia_masuk_kuliah = int (input ("berapa usia anda"))
lama_kuliah = int (input ("berapa usia anda(tahun)"))

usia_saat_ini = usia_masuk_kuliah + lama_kuliah
tahun_lulus = 2022 + lama_kuliah

print(f"saya, bernama {nama} berumur{usia_saat_ini}")
print(f"saya {nama}akan lulus pada tahun {tahun_lulus}")
