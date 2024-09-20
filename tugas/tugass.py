karakter1 = "Rofi" 
karakter2 = "Angga"
karakter3 = "Rifki"
uang = 50000

lokasi = input("Tentukan tempat: ")

print(f"{karakter1}: Hai kawan!ngomong ngomong gaada info keluar kota?, ayo kita main ke pantai{lokasi}.")
print(f"{karakter2}: Wah ide bagus tuh,kalo gitu mending sekarang aja ke pantai mumpung ada uang {uang}")
print(f"{karakter3}: Kalo aku sih ayo aja,sekarang hawa dingin enak soalnya aku suka hawa dingin.")
print(f"{karakter1}: Boleh tuh, tapi aku sekarang ga ada duit hehe.")
print(f"{karakter2}: Santai saja kawanku, aku ada uang ini ayo aku traktir.")
print(f"{karakter3}: Wahh boleh lah ya ditraktir kalo udah sampe pantai.")
print(f"{karakter1}: Wihh baik sekali. Terimakasih ya")
print(f"{karakter2}: Nanti kalo udah sampai beli es krim aja ya")
print(f"{karakter3}: Oke siap,yang penting nanti kamu yang bayar")
print(f"{karakter1}: Iya, yang penting nanti kamu traktir")

beli = int(input(f"{karakter2}: Masukkan jumlah es teh yang akan dibeli!!"))
harga = 10000
total = beli * harga
sisa = uang - total

print(f"{karakter2}: Oke, jadi kita beli {beli} es krim yaa. Harga satunya {harga} rupiah.")
print(f"{karakter3}: Berarti total belanjaan kita {total} rupiah.")
print(f"{karakter1}: Iya. tapi tunggu, berarti sisa uang {karakter2} tinggal {sisa} rupiah dong?")
print(f"{karakter2}: Iya tinggal segitu! Tapi gapapa,yang penting nanti kita bisa menikmati pemandangan pantai sambil menikmati eskrim {lokasi}.")
print(f"{karakter1}: Nah itu enak tuh! Yuk langsung aja kita berangkat ke {lokasi} sekarang.")
print(f"{karakter2}, {karakter3}: Yok Gasss berangkat...")

print(f"Akhirnya mereka bertiga pergi ke {lokasi} untuk menikmati indahnya pemandangan di pantai sambil menikmati eskrim mereka")