nama_tokoh1 = "Andi"
nama_tokoh2 = "Aurel"
ipk_tokoh1 = 4.00
ipk_tokoh2 = 3.23

# Program Cerita Pendek: Dialog Interaktif dengan Operasi Aritmatika
print("SELAMAT DATANG DI PROGRAM SAYA")
# Karakter pertama: Andi
nama_Andi = "Andi"
ipk_Andi = 4.00

# Karakter kedua: Andi
nama_Aurel = "Aurel"
ipk_Aurel = 3.22

# Dialog dimulai
print(f"{nama_Andi}: Hai {nama_Aurel}, bagaimana kabarmu hari ini?")
jawaban_Aurel = input(f"{nama_Aurel}: ")

print(f"{nama_Andi}: Senang mendengarnya! Ngomong-ngomong, kamu dapat ipk berapa, {nama_Aurel}?")
ipk_Aurel_input = int(input(f"{nama_Aurel}: ohh aku dapat ipk {ipk_Aurel}, kamu berapa, Andi? "))

# Menghitung perbedaan ipk
selisih_ipk = abs(ipk_Andi - ipk_Aurel)

print(f"{nama_Andi}: saya ipk nya{ipk_Andi} kita, jadi kita selisih  {selisih_ipk} !")

# Menggunakan operasi aritmatika untuk menghitung total ipk
total_ipk = ipk_Andi + ipk_Aurel
print(f"{nama_Andi}: Kalau kita gabungkan ipk kita, totalnya jadi {total_ipk} !")

# Andi ingin membeli minyak
print(f"{nama_Andi}: Aku ingin membeli 1 liter, harganya masing-masing Rp14.000. Berapa total yang harus kubayar?")
harga_minyak = 14.000
jumlah_harga_minyak = 1
total_harga = harga_minyak * jumlah_harga_minyak

print(f"{nama_Aurel}: Totalnya adalah Rp{total_harga}. Apakah uangmu cukup, Andi?")
uang_Andi = int(input(f"{nama_Aurel}: Aku punya uang Rp "))

# Memeriksa apakah uang Andi cukup
if uang_Andi >= total_harga:
    print(f"{nama_Aurel}: Uangmu cukup, kamu bisa membeli minyak!")
    sisa_uang = uang_Andi - total_harga
    print(f"{nama_Andi}: Setelah membeli minyak, uangku tersisa Rp{sisa_uang}.")
else:
    kekurangan = total_harga - uang_Andi
    print(f"{nama_Aurel}: Uangmu kurang Rp{kekurangan}. Kamu perlu menabung lebih banyak!")
# Cerita berakhir
print(f"{nama_Andi}: Terima kasih atas bantuannya, Aurel! Sampai jumpa di lain waktu.")
print(f"{nama_Aurel}: Sama-sama, Andi! Sampai jumpa.")

print("TERIMAKASIH DAN SAMPAI JUMPA")

