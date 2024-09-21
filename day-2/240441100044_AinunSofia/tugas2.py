nama ="Ainun"
umur = 18
profesi = "mahasiswa"
nama1 = "Rara"

print(f"{nama1}:Halo, nama kamu siapa?")
print(f"{nama}:Halo, nama aku {nama}")
print(f"{nama1}:Salam kenal aku {nama1}")
print(f"{nama1}:Btw kamu umur berapa?")
print(f"{nama}:aku {umur} tahun sekarang")

thh_skrg = 2024
thn_lahir = thh_skrg - umur 

print(f"{nama1}: Berarti kamu lahiran tahun {thn_lahir}?")
print(f"{nama}: Benar aku lahiran tahun {thn_lahir}")
print(f"{nama}: Kamu sendiri lahiran tahun berapa?")
lhr_thn = int(input(f"{nama1}: Aku lahiran tahun "))

umur1 = thh_skrg - lhr_thn

print(f"{nama}: Berarti kamu sekarang berumur {umur1} tahun?")
print(f"{nama1}: Yaps aku umur {umur1} tahun")
print(f"{nama1}: Kamu masih sekolah?")
print(f"{nama}: Aku sudah jadi {profesi} sekarang")
print(f"{nama1}: Wah {profesi}. Dimana kamu bersekolah ")
univ = str(input(f"{nama}: Aku kuliah di "))
print(f"{nama1}: Oalah di {univ}")
print(f"{nama}: Ingyah, Kamu sendiri gimana?")
univ1 = str(input(f"{nama1}: Aku mahasiswa di "))

if univ== univ1:
    print(f"{nama}: Wahh, rupanya kita satu tempat")
else:
    print(f"{nama1}: Oalahh, kirain sama kayak univ ku")

print(f"{nama1}: wkwkwk, kamu smt berapa sekarang?")
smt = int(input(f"{nama}: Sekarang aku semster "))

if smt== 1:
    print(f"{nama1}: Oalah angkatan 24")
elif smt== 3:
    print(f"{nama1}: Oalah angkatan 23")
elif smt== 5:
    print(f"{nama1}: Oalah angkatan 22")
elif smt== 7:
    print(f"{nama1}: Oalah angkatan 21")
else:
    print(f"{nama1}: Oalah semester {smt}")
exit()