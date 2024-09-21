# Definisikan variabel
karakter1 = "jarot" 
karekter2 = "sigit"

# Meminta input dari pengguna
print("selamat datang di cerita interaktif!")
umur_jarot = int(input("berapa usia jarot? "))
umur_sigit = int(input("berapa usia sigit? "))

# dialog antara jarot dan sigit 
print(f"\n{karakter1} : halo, {karekter2}! saya baru saja merayakan ulang tahun saya.")
print(f"{karekter2} : oh, selamat ulang tahun, {karakter1}! berapa umurmu sekarang?") 

# jarot memberi tahu umurnya dan sigit merespon
print(f"{karakter1} : terimakasih! sekarang umurku {umur_jarot} tahun.")
print(f"{karekter2} : wah, berarti kita memeliki selisih umur {umur_jarot-umur_sigit} tahun.")

hasil = umur_jarot > umur_sigit
print(f"apakah umur jarot lebih tua dari sigit?")
print(hasil)

# menutup dialog 
print(f"{karakter1} : terimakasih, {karekter2}! senang berbicara denganmu.")
print(f"{karekter2} : sama sama, {karakter1}! sampai jumpa!")