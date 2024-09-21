print ("selamat datang di dialog user dengan barista")

nama1 = input("masukkan user : ")
nama2 = ("Barista")

print (nama2, ": Selamat Datang Mas, Mau pesan apa ? ")
input (nama1)
print (nama2, ": Baik, Silahkan di tunggu")
print (nama1, ": Baik Mbak")
print ("==selang beberapa menit pesanan", nama1, "datang==")
input ("tekan enter untuk melanjutkan dialog")
print (nama2, ": Ini pesanannya")
print (nama1, ": oia disini ada nuget gak mbak")
print (nama2, ": ada, mau pesen berapa porsi ?")
variabel = int(input ("Silahkan masukkan angka : "))

if variabel < 2 :
    print(nama2, ": baik satu porsi ya")
    print (nama1,": iya mbak")
elif variabel == 1 :
    print (nama2, ": baik silahkan di tunggu")
    print (nama1, ": baik mbak")
else :
    print(nama2, ": maaf ini tinggal satu porsi")
    print(nama1,": oiya mbak gapapa satu aja")

input("enter untuk next ")

print ("==selang beberapa menit pesanan", nama1, "datang==")
input ("tekan enter untuk melanjutkan dialog")
print (nama2, ": ini nugetnya")
print (nama1, ": baik mbak, terimakasih")
print ("==setelah makan", nama1, "membayar pesanannya==")
print (nama1, "totalnya berapa mbak, semuanya")
print ("===tolong bantu barista menghitung===")

variabel1 = int(input("masukkan harga pesanan pertama : "))
variable2 = int(input ("masukkan harga pesanan kedua : "))

hasil =(variabel1 + variable2)

print("total semua adalah : ", hasil)

print("==selesai==")