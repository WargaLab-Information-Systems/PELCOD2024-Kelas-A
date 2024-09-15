beledos = "pavellino alvian syah"
nim = 240441100084
ipk = 4.00
mahasiswa = True

# ini adalaha format natural(tipe data sama)
print("nama saya adalah", beledos)
print("nim saya adalah", nim)
print("impian ipk saya adalah", ipk)
print("saya merupakan mahasiswa ", mahasiswa)

# ini adalah format string (tipe data diubah menjadi string)
print(f'nama saya adalah {beledos}')
print(f'nim saya adalah {nim}')
print(f'ipk saya adalah {ipk}')
print(f'mahasiswa saya adalah {mahasiswa}')

#program dinamis string
nama_panjang = str(input("nama saya adalah : "))

#program dinamis intejer
nilai_matematika = int(input("nilai saya adalah : "))

nilai_matematika = 60
nilai_biologi = 89
nilai_kimia = 60
nilai_fisika = 90

T = nilai_matematika * nilai_kimia
K = nilai_biologi + nilai_fisika
P = nilai_kimia - nilai_matematika
B = nilai_kimia / nilai_fisika

print(f'hasil penjumlahan dari matematika dan kimia adalah : {T}')
print(f'hasil perkalian dari biologi dan fisika adalah : {K}')
print(f'hasil pengurangan dari biologi dan fisika adalah : {P}')
print(f'hasil pembagian dari biologi dan fisika adalah : {B}')




usia_masuk_kuliah = int(input("berapa usia anda saat masuk kuliah ?"))
lama_kuliah = int(input("berapa lama anda kuliah ?"))

usia_saat_ini = usia_masuk_kuliah + lama_kuliah
tahun_lulus = 2024 + lama_kuliah

print(f'saat ini, saya {beledos} berumur {usia_saat_ini}')
print(f'saya {beledos} saya lulus pada tahun  {tahun_lulus}')