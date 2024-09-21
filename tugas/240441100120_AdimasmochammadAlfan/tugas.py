# tentukan variabel dan type data terlebih dahulu
orang1 = "adimas"
orang2 = "jidan"

print(f"pada suatu hari saat libur semester {orang1} sedang jalan-jalan ditaman yang dekat dengan rumahnya, tak lama {orang1} melihat temannya yang sedang duduk di taman")
print(f"==================================================================")
print(f"*{orang1} menghampiri {orang2}")
# lalu buatlah sebuah percakapan

print(f"{orang1} : halo {orang2} apa kabar kau sehat ?")
print(f"{orang2} : wih {orang1}, alhamdulilah nih sehat")
print(f"{orang1} : owalah bagus deh kalo gitu")
print(f"{orang2} : oh iya, ini kan udah mau libur semester {orang1} nggak ada rencana mau liburan ? (pengen sih/ nggak pengen)")
jawaban = input(f"{orang1} : ")

if jawaban.lower() == "pengen sih":
    print(f"{orang2} : wih jalan jalan jauh dong")
else:
    print(f"{orang2} : sama sih, aku juga nggak pengen. nyaman di rumah aja")

print(f"{orang1} : iya nih pengennya gitu")
print(f"{orang2} : eh kemarin kan ada penugasan disuruh bawa buah apel")
print(f"{orang1} : iya aku udah beli buah nya")
print(f"{orang2} : iya kah ?")

# input untuk data penugasan buah apel
buah_apel_adimas =int(input(f"{orang1} : iya, aku cuma beli "))
buah_apel_jidan =int(input(f"{orang2} : aku beli "))

# menghitung data berbeda penugasan buah apel
selisih_buah_apel =abs(buah_apel_adimas - buah_apel_jidan)

# lanjut dengan penyeleksian untuk menentukan kondisinya
if buah_apel_adimas>buah_apel_jidan:
    print(f"{orang1} : loh ternyata punya aku lebih banyak {selisih_buah_apel} buah ya dari kau {orang2}")
elif buah_apel_adimas<buah_apel_jidan:
    print(f"{orang1} : loh ternyata punya aku lebih sedikit {selisih_buah_apel} buah ya dari kau {orang2}")
else:
    print(f"{orang1} : loh ternyata sama ya jumlahnya")
    
# lalu masukkan data operasi aritmatika lain
total_buah_apel = buah_apel_adimas * buah_apel_jidan
total_dibagikan_dua =int(total_buah_apel / 2)
print(f"{orang2} : Dim kalo kita kalikan dan hasinya dibagi 2 jadi berapa ya ?")
print(f"{orang1} : hmmm sebentar ngitung dulu")
print(f"{orang2} : buah apel punya mu kan {buah_apel_adimas}, sedangkan buah apel ku kan {buah_apel_jidan}")
print(f"{orang1} : jadi kalau di kalikan hasilnya jadi {total_buah_apel} buah")
print(f"{orang2} : dan hasil yang dikalikan tadi dibagi 2 jadi {total_dibagikan_dua} buah")
print(f"{orang1} : ohh jadi begitu ya, oke deh aku pulang dulu ya {orang2}")
print(f"{orang2} : oh iya {orang1} aku juga mau pulang")
print(f"{orang1} : yaudah bye dan")
print(f"{orang2} : bye juga dim")
print(f"=================================== TAMAT ===============================")
