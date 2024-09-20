nama1 = "Jefri"
nama2 = "Sekar"
nama3 = "Buk Lis"
fakultas = "Teknik"
prodi1 = "Sistem Informasi"
prodi2 = "Teknik Sipil"

print("Disuatu hari saat selesai mata kuliah ada 2 seseorang yang tak sengaja bertemu di kantin lalu mereka berkenalan")

print(f"{nama1}: hai, boleh aku duduk di sini ya?")
print(f"{nama2}: haloo, boleh kok boleh. Nama kamu siapa?")
print(f"{nama1}: oh yaa, kenalin nama aku {nama1}. Kalo kamu?")
print(f"{nama2}: nama aku {nama2}, salam kenal ya {nama1}")

print(f"{nama1}: btw kamu dari fakultas apa prodi apa {nama2}?")
print(f"{nama2}: aku dari fakultas {fakultas} prodi {prodi2}")
print(f"{nama1}: lohh sama dong aku juga dari fakultas {fakultas} tapi prodi {prodi1}, jangan jangan kita...")
print(f"{nama1}: bercanda kok, hehe")
print(f"{nama1}: hahaha iya aman {nama1}")

print("setelah mereka berkenalan, mereka memesan minuman di kantin tersebut")

pesan = input(f"{nama1}: eh kamu haus ga {nama2} pesan minum ayo?!, mau pesan apa kamu?")

if pesan == "ayo, es teh saja":
    print(f"{nama1}: berarti es teh 1 dan es jeruk 1 yaa {nama3}")
    print(f"{nama3}: siapp dek {nama1}")

print("setelah memesan minuman jefri mempunyai inisiatif untuk mengajak sekar bermain badminton")

print(f"{nama1}: kamu besok ada waktu kosong ga {nama2}?")
print(f"{nama2}: kebetulan ada, besok cuman ada kelas pagi, kenapa jef?")
print(f"{nama1}: wuihh kebetulan banget nih, gimana kalau kita main badminton di timur kampus, kamu mau tidak {nama2}?")

waktu = int(input(f"{nama2}: boleh bolehh, jam berapa besok jef?"))

if waktu > 0 and waktu <= 24:
    print(f"{nama2}: okee, besok jam segitu di timur kampus yaa!")

print(f"{nama1}: okee siap, yaudah pulang yuk mau hujan, bayar dulu")

print("akhirnya mereka ingin pulang dan membayar minuman yang mereka pesan tadi")

print(f"{nama1}: berapa total semuanya {nama3}?")

es_teh = int(input(f"{nama3}: es teh nya"))
es_jeruk = int(input(f"{nama3}: es jeruk nya"))

total = es_teh + es_jeruk

print(f"{nama3}: total semuanya {total} dek {nama1}")
print(f"{nama1}: ini yaa {nama3} uang pas, terimakasih bukk!")
print(f"{nama3}: iyaa dek {nama1} sama-sama")
print(f"{nama2}: berapa yang aku jef?")
print(f"{nama1}: gausaa wes")
print(f"{nama2}: loh loh loh")
print(f"{nama2}: gapapaa santai aaman")
print(f"{nama2}: makasii yaa {nama1}")
print(f"{nama1}: iyaa sama-sama {nama2}")

print("dan mereka pulang ke kostnya masing-masing")
print("~TAMAT~")

    
