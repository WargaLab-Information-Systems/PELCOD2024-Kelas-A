# Inisialisasi variabel
arif_age = ()
vincent_age = ()

# Mulai percakapan
print("Arif: Halo Vincent! Berapa umurmu sekarang?")
vincent_age = int(input("Vincent: Umurku "))

print(f"Vincent: Umurku {vincent_age} tahun. Kalau kamu arif?")
arif_age = int(input("Arif: Aku berumur "))

# Operasi aritmatika
age_difference = abs(vincent_age - arif_age)

print(f"Arif: Hmmm, selisih umur kita {age_difference} tahun!")

# Operasi logika
if vincent_age > arif_age:
    print("Vincent: Iya, aku lebih tua darimu.")
elif vincent_age < arif_age:
    print("Vincent: Ternyata kau lebih tua dariku.")
else:
    print("Vincent: Wah, ternyata umur kita sama yaaa!")

# Input pengguna untuk hobi
arif_hobby = input("Arif: Btw, apa hobimu, Vincent? ")
print(f"Vincent: Oh, hobiku adalah {arif_hobby}. Kalau lu?")
vincent_hobby = input("Arif: Hobiku ")

# Operasi logika untuk membandingkan hobi
if arif_hobby.lower() == vincent_hobby.lower():
    print("Vincent: Wah, hobi kita samaan nih!")
else:
    print("Vincent: Menarik juga hobi kita berbeda.")

# Operasi aritmatika dengan input pengguna
print("Arif: eh, ayo main tebak-tebakan yok!")
number1 = int(input("Arif: Berapa 5 x 7? "))
correct_answer = 5 * 7

if number1 == correct_answer:
    print("Arif: Benar sekali! Kamu pintar matematika ya.")
else:
    print(f"Arif: Hmm, sebenarnya jawabannya adalah {correct_answer}.")

print("Arif: aku ada tebak - tebakan lagi nih!!!")
number2 = int(input("Arif: Berapa kelipatan angka perhitungan data pada komputer? "))
correct_answer = 2

if number2 == correct_answer:
    print("Arif : Benar sekali!")
else:
    print(f"Arif : Hmm, sebenarnya jawabannya adalah {correct_answer}.")

print("Arif: Terima kasih Vincent, senang ngobrol denganmu!")
print("Vincent: Sama-sama arif, sampai jumpa lagi!")