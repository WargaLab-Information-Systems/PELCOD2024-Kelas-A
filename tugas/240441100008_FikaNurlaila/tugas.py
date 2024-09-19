#variabel
nama_pemain_1="hema"
nama_pemain_2="fika"
nama_pemain_3="isti"
tempat="nganjuk"
kota="tulungagung"
waktu="15 menit"
hapytos=15000
citato=8000
aoka=5000
es=25000

#tipe data
print("cuaca hari ini sangatlah bagus,sehingga kami berdua pergi kepantai")
print(f"{nama_pemain_1} dan {nama_pemain_2} pergi kepantai menggunakan motor, karena jarak {tempat} menuju {kota} cukup dekat,hanya membutuhkan {waktu} untuk menempuhnya")
print()

print(f"{nama_pemain_1}: \"semilir angin dipantai sejuk yha {nama_pemain_2}\"")
print(f"{nama_pemain_2}: \"iyha, apalagi sambil menikmati es kelapa muda yang seger\"")
print(f"{nama_pemain_1}: \"eh iya, kita beli es kelapa muda yukk\"")
print(f"{nama_pemain_2}: \"gimana kalau kita belinya di toko dekat pepohonan itu ?\"")
print(f"{nama_pemain_1}; \"kamu duduk disini saja biar aku yang membelinya\"" )
print(f"{nama_pemain_2}: \"baiklah kalau begitu\"")
print(f"{nama_pemain_1}: \"oke\"")
print()

print(f"setelah itu {nama_pemain_1} bergegas menuju toko yang tadi diberitahu oleh {nama_pemain_2}")
print(f"{nama_pemain_1}: \"permisi bu\"")
print(f"{nama_pemain_3}: \"iya kak, mau beli apa ?\"")
print(f"{nama_pemain_1}: \"saya ingin memebeli es kelapa muda dan beberapa cemilan\"")
print(f"{nama_pemain_3}: \"baik kak, silahkan kakak memilih memilih cemilan, saya buat kan es kelapa mudanya dulu\"")
print(f"{nama_pemain_1}: \"baik bu, untuk totalnya berapa yha ?\"")
print(f"{nama_pemain_3}: \"baik , untuk cemilannya kakak apa saja ?\"")
print(f"{nama_pemain_1}: \"saya beli hapytos 2, citato 2, aoka 4, dan es kelapa mudanya 2\"")
print(f"{nama_pemain_3}: \"baik, saya total dulu\"")

#operasi aritmatika & operasi logika
uang_pemebeli=150000
total_hapytos=hapytos*2
total_citato=citato*2
total_aoka=aoka*4
total_es=es*2
total_belanja=total_hapytos+total_citato+total_aoka+total_es
if total_belanja>100000:
    diskon=total_belanja*0.05
    total_bayar=total_belanja-diskon
print(f"{nama_pemain_3}: \"untuk harga hapytosnya {total_hapytos}, citatonya {total_citato}, aokanya {total_aoka}, dan es kelapa mudanya {total_es}, jadi total belanja keseluruhan {total_hapytos+total_citato+total_aoka+total_es} dan kakak mendapatkan diskon 5%! jadi total harga setelah diskon: Rp{total_bayar}\"")
print(f"{nama_pemain_1}: \"ini buk uang nya {uang_pemebeli}")
print(f"{nama_pemain_3}: \"iya kak, untuk kembaliannya {uang_pemebeli-total_bayar} ya kak, terima kasih telah berbelanja di toko kami:)\"")
print(f"{nama_pemain_1}: \"sama sama buk, mari\"")
print()

#menerima input dari pengguna
yha="1"
tidak="0"
print("bagaimana dengan cerita di atas? apakah anda suka? jawab 1 yha (kalau kamu suka) / 0 tidak (kalau kamu tidak suka)")
jawab=input()
if jawab=="1":
    print("terima kasih sudah menyukai cerita saya :)")
else :
    print("terima kasih pendapatnya, saya akan berusaha memperbaikinya menjadi lebih bagus lagi :)")