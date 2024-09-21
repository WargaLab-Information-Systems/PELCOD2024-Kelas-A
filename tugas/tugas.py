farelage = ()
siti_age = ()

# Mulai percakapan
print("farel: Halo siti! Berapa umurmu sekarang?")
siti_age = int(input("siti: Umurku "))

print(f"siti: Umurku {siti_age} tahun. Kalau kamu farel?")
farelage = int(input("farel: Aku berumur "))

#Operasi arimatika
age_difference = abs(siti_age - farelage)

print(f"farel: Hmm, selisih umur kita {age_difference} tahun!")

#Operasi logika
if siti_age > farelage:
    print("siti: Iya, aku lebih tua darimu.")
elif siti_age < farelage:
    print("siti: Ternyata kamu lebih tua dariku.")
else:
    print("siti: Wah, ternyata umur kita sama yaa!")

#input pengguna untuk hobi
farel_hobby = input("farel: Btw, apa hobimu, siti? ")
print(f"siti: Oh, hobiku {farel_hobby}. Kalau lu?")
siti_hobby = input("farel: Hobiku ")

#operasi logika untuk membandingkan hobi
if farel_hobby.lower() == siti_hobby.lower():
    print("siti: Wah, hobi kita samaan nih!")
else:
    print("siti: Menarik juga hobi kita berbeda.")