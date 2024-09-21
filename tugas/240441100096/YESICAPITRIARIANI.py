nama1 = "yesica"
nama2 = "yeyen"
umur1 = "19 tahun"
umur2 = "18 tahun"
tahun_kelahiran1 = "2005"
tahun_kelahiran2 = "2005"

print("ditempat yaitu kantin ada dua orang mahasiswa yang saling sapa dan berkenalan")

print("yeyen : hallo,siapa nama kamu?")
print("yesica : hai namaku", nama1)

print("yesica : eh iya nama kamu siapa?")
print("yeyen : namaku", nama2)

print("yeyen : eh kalau boleh tau kamu kelahiran tahun berapa,takut kalau tuaan kamu biar ku panggil kakak?")
print("yesica : aku kelahiran tahun" , tahun_kelahiran1)

print("yesica : kalau kamu kelahiran tahun berapa?")
print("yeyen : aku kelahiran" , tahun_kelahiran2)

print("yeyen : oala jadi kamu sekarang umur berapa?")
print("yesica : umur aku sekarang",umur1)

print("yesica : kalau kamu sekarang umur berapa?")
print("yeyen : umur aku sekarang",umur2)

yesica = input("yesica : eh yen beli bolpoin yuk di toko depan kampus")
yeyen = input("yeyen : yuk kebetulan bolpoin ku udah habis juga")

if yesica == "yuk" and yeyen == "okei":
   print("yuk beli bolpoin")

print("terus mereka berjalan menuju depan kampus untuk membeli bolpoin")

print("selesai memilih bolpoin mereka membayar ke ibu penjualnya")
print("mereka berdua pun mulai berdialog")

print("yesica : eh harga bolpoin kamu berapa?")
print("yeyen : harga bolpoin aku 4000, punya kamu berapa?")
print("yesica : harga bolpoinku 3000")

duwek = input("ini bayarnya di jadikan satu aja?")
uang = input("berapa total semuanya?")


if duwek == "yuk" and uang == "hayuk hita hitung dulu":
   print("masukkan harga bolpoin yeyen")
   print("masukkan harga bolpoin yesica")

bil1hargabolpoinyeyen = int(input("masukkan harga bolpoin yeyen"))
bil2hargabolpoinyesica = int(input("masukkan harga bolpoin yesica"))

hasil = bil1hargabolpoinyeyen + bil2hargabolpoinyesica

print("hasil penjumlahan dari" , bil1hargabolpoinyeyen , "ditambah" , bil2hargabolpoinyesica , "adalah" , hasil)

print("akhirnya mereka berdua membayar bolpoinnya dengan harga RP7000 ke ibu yang jualan bolpoin")

print("akhirnya dialog ini selesai")

