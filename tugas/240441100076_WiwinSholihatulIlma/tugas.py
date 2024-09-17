orang1 = "vino"
orang2 = "satrio"

print(f"{orang1} : Halo, apa kabar")
print(f"{orang2} : Iya halo, kabar baik, kamu sendiri?")
print(f"{orang1} : Kabarku baik")
print(f"{orang1} : Kenalin namaku vino")
print(f"{orang2} : hai,kenalin juga namaku satrio")

print(f"{orang1} : Eh kamu kos di telang indah gang 1 Ya?(ya/tidak)")
Jawaban=(input(f"{orang2} : "))

if Jawaban.lower() == "ya":
    print(f"{orang2} : Iya nih kenapa emang")
else:
    print(f"{orang2} : Enggak aku pp")

print(f"{orang1} : oala sama donggg")
print(f"{orang1} : btw, kamu angkatan berapa?")

angkatan1=int(input(f"{orang2} : aku angkatan :"))
angkatan2=int(input(f"{orang1} : oh kalau aku angkatan :"))

perbedaan_angkatan=abs(angkatan1-angkatan2)

if perbedaan_angkatan == 0:
    print(f"{orang2}  oalah kita satu angkatan ternyata")
else:
    print(f"{orang2} : oalah ternyata kita beda {perbedaan_angkatan} tahun")
    