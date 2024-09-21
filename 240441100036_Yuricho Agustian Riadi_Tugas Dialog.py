# Karakter
karakter1 = "Akmal"
karakter2 = "Rafi"

# Meminta input dari pengguna
usia_akmal = int(input(f"Berapa usia {karakter1}? "))
usia_rafi = int(input(f"Berapa usia {karakter2}? "))

# Operasi logika
if usia_akmal > usia_rafi:
    print(f"{karakter1}: Aku lebih tua dari {karakter2}.")
elif usia_akmal < usia_rafi:
    print(f"{karakter2}: Aku lebih tua dari {karakter1}.")
else:
    print(f"{karakter1} dan {karakter2} sama-sama tua.")

# Operasi aritmatika
total_usia = usia_akmal + usia_rafi
print(f"{karakter1}: Total usia kita berdua adalah {total_usia} tahun.")

# Meminta input untuk aktivitas
aktivitas = input(f"{karakter2}: Apa kita mau beraktivitas hari ini? (ya/tidak) ")

# Logika berdasarkan input aktivitas
if aktivitas.lower() == "ya":
    print(f"{karakter1}: Ayo kita bermain!")
else:
    print(f"{karakter2}: Baiklah, kita istirahat saja.")
