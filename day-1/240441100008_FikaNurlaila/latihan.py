nama="Fika Nurlaila"
nim=240441100008
ipk=4.00
mahasiswa=True

#ini adalah format natural(tipe data sama)
print("perkenalkan nama saya",nama)
print("dengan NIM",nim)
print("impian ipk saya adalah",ipk)
print("saya merupakan mahasiswa",mahasiswa)

#ini adalah format string(tipe data diubah menjadi string)
print(f'nim saya adalah{nim}')

#program dinamis string
nama_panjang = str(input("perkenalkan nama saya:",nama))

#program dinamis integer
nilai_matematika = int(input("nilai saya adalah:"))

nilai_matematika = 89
nilai_biologi = 75
nilai_kimia = 90
nilai_fisika = 83

penjumlahan = nilai_matematika + nilai_kimia
perkalian = nilai_matematika * nilai_kimia
pengurangan = nilai_matematika - nilai_kimia
pembagian = nilai_matematika / nilai_kimia

int(f'hasil penjumlahan dari matematika dan kimia adalah : {penjumlahan}')
int(f'hasil perkalian dari matematika dan kimia adalah : {perkalian}')
int(f'hasil pengurangan dari matematika dan kimia adalah : {pengurangan}')
int(f'hasil pembagian dari matematika dan kimia adalah : {pembagian}')

usia_masuk_kuliah = int(input("berapa usia anda ?"))
lama_kuliah = int(input("berapa lama anda kuliah (tahun) ?"))

usia_saat_ini = usia_masuk_kuliah + lama_kuliah
tahun_lulus = 2024 + lama_kuliah

print(f'saat ini, saya {nama} berumur {usia_saat_ini}')
print(f'saya {nama} akan lulus pada tahun {tahun_lulus}')
