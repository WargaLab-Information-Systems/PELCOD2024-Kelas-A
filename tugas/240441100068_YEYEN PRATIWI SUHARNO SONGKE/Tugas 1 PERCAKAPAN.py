#inisialisasi varibel karakter
nama_karakter1="puput"
nama_karakter2="Sani"

#Dialog awal
print(f"\n{nama_karakter1}:{nama_karakter2}?")
print(f"\n{nama_karakter1}:Hai,{nama_karakter2} Aku {nama_karakter1}!bisakah kau membantuku?.")
print(f"\n{nama_karakter2}:Hai juga {nama_karakter1},Tentu saja apa yang bisa ku bantu?")

#input untuk operasi aritmetika
Angka1=int(input(f"\n{nama_karakter1}:Aku punya sebuah angka tolong bantu aku menyelesaikanya angka pertama: "))
angka2=int(input(f"\n{nama_karakter2}:Dan angka kedua?"))

#Melakukan operasi aritmetika
jumlah= Angka1 + angka2
selisi= Angka1 - angka2
pembagian= Angka1 * angka2
if angka2 !=0:
   pembagian=Angka1/angka2
   
else:
    pembagian=None

#Menampilkan hasil operasi
print(f"\n{nama_karakter1}:Hasl dari {Angka1} + {angka2} adalah {jumlah}")
print(f"\n{nama_karakter2}:Hasil dari {Angka1} - {angka2} Adalah {selisi}")
print(f"\n{nama_karakter1}:Hasil dari {Angka1} * {angka2} adalah {pembagian}")

#Dialog Akhir 
print(f"\n{nama_karakter1}:Makasi atas bantuanya {nama_karakter2}")
print(f"\n{nama_karakter2}:iya sama sama {nama_karakter1},Senang bisa membantumu")


