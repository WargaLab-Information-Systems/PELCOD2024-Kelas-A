# Dialog antara dua orang dengan penambahan aritmatika dan logika
def dialog():
    # Orang pertama berbicara
    print("Orang 1: Aku sedang berpikir, kalau aku punya 5 apel dan kamu punya 3 apel, berapa total apel kita?")
    
    # Operasi aritmatika untuk menghitung total apel
    apel_orang1 = 5
    apel_orang2 = 3
    total_apel = apel_orang1 + apel_orang2
    
    # Orang kedua menjawab
    print(f"Orang 2: Kalau begitu, totalnya adalah {total_apel} apel.")
    
    # Orang pertama berbicara lagi
    print("Orang 1: Benar! Nah, kalau kita membagi rata apel kita, berapa yang kita dapatkan masing-masing?")
    
    # Operasi aritmatika untuk membagi apel secara rata
    apel_per_orang = total_apel / 2
    
    # Orang kedua menjawab
    print(f"Orang 2: Kita masing-masing dapat {apel_per_orang} apel.")
    
    # Logika sederhana
    print("Orang 1: Kalau aku punya lebih dari 4 apel, apakah aku punya lebih banyak apel darimu?")
    
    # Operasi logika untuk memeriksa siapa yang punya lebih banyak apel
    if apel_orang1 > apel_orang2:
        print("Orang 2: Ya, kamu punya lebih banyak apel daripada aku.")
    else:
        print("Orang 2: Tidak, kita punya jumlah apel yang sama atau aku punya lebih banyak.")
    
    # Penambahan logika dengan operasi AND
    print("Orang 1: Dan jika kita sama-sama punya lebih dari 2 apel, apakah kita termasuk beruntung?")
    
    # Operasi logika AND untuk memeriksa apakah keduanya punya lebih dari 2 apel
    if apel_orang1 > 2 and apel_orang2 > 2:
        print("Orang 2: Ya, kita beruntung!")
    else:
        print("Orang 2: Tidak, salah satu dari kita tidak beruntung.")

# Memanggil fungsi dialog
dialog()
