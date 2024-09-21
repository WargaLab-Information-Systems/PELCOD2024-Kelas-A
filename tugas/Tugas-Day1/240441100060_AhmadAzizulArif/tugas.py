# Variabel
karakter1 = "Mursyid"
karakter2 = "Vincent"
karakter3 = "Pascol"

# Hasil acak dari 1 - 5
import random
posisi_bola = random.randint(1, 5)

# Bertemunya karakter 1, 2, dan 3
print(f"{karakter1} : Halo {karakter2} dan {karakter3} Mau kemana kalian")
print(f"{karakter2} : Gak kemana-mana, disini aja")
print(f"{karakter1} : Ayo kita duduk disana")
print(f"{karakter2} dan {karakter3} : Ayo...")

# Bermain tebak-tebakan
print(f"{karakter1} : Ayo kita main tebak-tebakan biar gak bosen")
print(f"{karakter2} dan {karakter3} : Ayo...")
print(f"{karakter1} : Kalau aku punya 15 pisang dan kubagikan kepada 3 orang yang membutuhkan, berapa pisang yang didapat masing-masing orang itu?")
print(f"{karakter3} : Waduh aku gak bisa matematika, kamu tau nggak {karakter2}?")
jawaban_pisang = int(input(f"{karakter2} : "))

# Rumus bermain tebak-tebakan
if jawaban_pisang == 15 / 3:
    print(f"{karakter1} : Betul sekali {karakter2}, masing-masing orang dapat 5 pisang")
else:
    print(f"{karakter1} : Sayang sekali {karakter2}, jawaban mu salah yang benar adalah 5 pisang")

print(f"{karakter1} : Gimana nih {karakter3} kamu gak bisa jawab")
print(f"{karakter3} : Mau gimana lagi aku gak bisa Matematika, ada permainan lain gak?")
print(f"{karakter1} : Ada ")

# Game baru mencari bola
print(f"{karakter1} : Ada 5 gelas didalam gelas ada 1 bola nah kalau kamu bisa menemukan bola itu kamu akan aku kasih hadiah uang gimana mau?")
print(f"{karakter3} : Mau dong")
print(f'''{karakter1} : oke, sekarang pilih 1 gelas di bawah ini
 _   _   _   _   _
| | | | | | | | | |
 1   2   3   4   5''')

# Jawaban karakter 3
pilihan_karakter3 = int(input(f"{karakter1} : Sekarang tebak bolanya ada di gelas nomer berapa? "))
konfirmasi_karakter3 = input(f"{karakter1} : Apakah kamu sudah yakin {karakter3} kalau bolanya ada disana, kalau kamu gak yakin mainnya gak jadi aku mau pulang gimana yakin apa tidak? [y/n] ")

# Rumus mencari bola
if konfirmasi_karakter3 == "y":
    if pilihan_karakter3 == posisi_bola:
        print(f"{karakter1} : Selamat {karakter3} pilihan kamu benar, ini hadiahnya daun. KabUuUuRrr...")
        print(f"{karakter3} : Woy {karakter1} malah dikasih daun, jangan kabur kamu")
    else:
        print(f"{karakter1} : Sayang sekali {karakter3} posisi bola nya ada di gelas nomer {posisi_bola}. Sedangkan kamu memilih gelas nomer {pilihan_karakter3}")
        print(f"{karakter3} : yah salah :( ")
        print(f"{karakter1} : Udah malem nih aku mau balik dulu besok kita main lagi yaa..")
        print(f"{karakter2} dan {karakter3} : iya hati-hati")
else:
    print(f"{karakter1} : Yaudah aku balik dulu, babay")
    print(f"{karakter2} : Ih kamu gimana sih {karakter3} tinggal jawab yakin aja biar {karakter1} gak pulang.")
    print(f"{karakter3} : Kasian juga udah mau malem, rumah dia kan jauh, tunggu besok aja")
    print(f"{karakter2} : Yaudah kalo gitu aku juga balik, babay")
    print(f"{karakter3} : Iya hati-hati")