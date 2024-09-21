nama_dila = "Dila"
nama_dzaki = "Dzaki"
nama_nabila = "Nabila"

print(f"Dila : Halo, kalian ! Besok ada mata kuliah apa?")
print(f"Dzaki : Halo, Dila ! Besok ada mata kuliah Logika Engineering.")
print(f"Nabila : Oh iya, minggu kemarin kita belajar tentang Operasi Aritmatika, kan?")
print(f"Dila : Itu gimana, sih? Aku kurang faham.")
print(f"Dzaki : Jadi gini, misal kita mau menghitung harga ayam geprek dan es jeruk.")

harga_ayam_geprek = int(input("Dzaki: Masukkan harga ayam geprek :"))
harga_es_jeruk = int(input("Dzaki: Masukkan harga es jeruk :"))

harga_ayam_geprek = 6000
harga_es_jeruk = 5000

hasil = harga_ayam_geprek+harga_es_jeruk
print(f"Dzaki: Ini adalah total harga dari ayam geprek ditambah es jeruk = 11000")
print(hasil)

print(f"Dzaki: Nah, gitu. Faham gak kalian?")
print(f"Dila: Begitu ya, oke faham aku. Terus kita kemarin juga belajar tentang Operasi Logika, kan?")
print(f"Nabila: Iya, kalau itu bagaimana?")
print(f"Dzaki: Jadi gini, kita tentukan dulu nilai untuk A dan B.")

def negasi(x):
    return not x

def konjungsi(x, y):
    return x and y

def disjungsi(x, y):
    return x or y

A = input(f"Dila: Nilai untuk A (Benar/Salah): ").capitalize() == "Benar"
B = input(f"Nabila: Nilai untuk B (Benar/Salah): ").capitalize() == "Salah"

print(f"Dzaki: Oke, A = {A} dan B = {B}")

print(f"Dila: Apa hasil dari negasi A?")
hasil_negasi_A = negasi(A)
print(f"Dzaki: Negasi A adalah: {hasil_negasi_A}")

print(f"Nabila: Bagaimana jika ada konjungsi (AND) antara A dan B?")
hasil_konjungsi = konjungsi(A, B)
print(f"Dzaki: Hasil dari A AND B adalah: {hasil_konjungsi}")

print("Dila: Bagaimana jika ada disjungsi (OR) antara A dan B?")
hasil_disjungsi = disjungsi(A, B)
print(f"Dzaki: Hasil dari A OR B adalah: {hasil_disjungsi}")

print(f"Dzaki: Nah, begitu lah sekilas tentang Operasi Logika.")
print(f"Nabila: Terimkasih ya Dzaki, atas penjelasannya.")
print(f"Dila: Iya Dzaki, terimakasih ya.")
print(f"Dzaki: Sama-sama.")