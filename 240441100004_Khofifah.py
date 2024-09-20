# nama="Khofifah"
# nim=2404411004
# ipk=4.00
# mahasiwa=True


# print("Nama saya",nama)
# print("Nim saya",nim)
# print("Ipk saya",ipk)
# print("saya seorang mahasiswa ",mahasiwa)

orang1="khofifah"
orang2="nayzila"
#Percakapan Pertama
print(f"{orang1} : Halo nayzila, apa kabar")
print(f"{orang2} : eh iya halo {orang1} kabarku baik")

jawaban = (input(f"{orang1} : kamu asal sumenep ya ? "))
if jawaban == "ya":
    print(f"{orang2} : aku orang sumenep")
else:
    print(f"{orang2} : aku bukan orang sumenep")

jawaban = (input(f"{orang1} : uang bulananmu berapa ? "))
if jawaban == "500.000 ya ?":
    print(f"{orang2} : iya uang bulananku 500.000")
else:
    print(f"{orang2} : tidak uang bulananku 1.000.000")

print(f"{orang1} : wah uang bulanan kita sama")
jawaban = (input(f"{orang2} : kalo uang bulananmu 1 bulan 500.000 berarti satu semester berapa ? "))
if jawaban == "bentar bentar aku hitung dulu" :
    print(f"{orang2} : okeyy")
else :
    print(f"{orang2} : ohh")
print(f"{orang1} : jawabannya")
satu_bulan = 500.000
satu_semester = 6
hasil = satu_bulan * satu_semester 
print(satu_bulan, '*',satu_semester, '=',hasil)
print(f"{orang1} : 3.000.000 persemesternya")
print(f"{orang2} : wah,cepat banget kamu ngehitungnya")
print(f"{orang1} : hehehe,iya terimakasih")

