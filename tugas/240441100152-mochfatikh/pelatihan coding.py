orangpertama ="fatikh"
orangkedua = "akhmed"
alamat1 ="sidoarjo"
alamat2 ="surabaya"
kelas1 = "rkbf lantai 2"
kelas2 = "rkbf lantai 3"

print(f"pada suatu hari aku sedang ingin ke perpus,aku sangat buru-buru karna ada suatu hal penting. tiba tiba aku disenggol oleh seseorang \n")
print(f"{orangpertama} : aduh,* buku berjatuhan")
print(f"{orangkedua} : sini biar aku bantu")
print(f"{orangpertama} : oh iya terima kasih sudah membantu")
print(f"{orangkedua} :hei tunggu sebentar? ")

print(f"{orangpertama} : iya ada apa?")
print(f"{orangkedua} : sepertinya aku kenal kamu deh kamu {orangpertama} kan")
print(f"{orangpertama} :iyaa kamuuu {orangkedua} kan ?")
print(f"{orangkedua} : iyaa, kita kan temen sd waktu dulu kita bareng terus")

print(f"{orangpertama} :oh iya kan kita perna satu sd dulu.aku duluan ya med aku lagi buru buru")
print(f"{orangkedua} :heyy tunggu minta no hp kmu dong?")
print(f"{orangpertama} :emm aku lupa kamu follow ig ku aja @ftkhrhmdn_")
print(f"{orangkedua} :iyaaa okee nanti aku follow ")
print(f"{orangpertama} :iyaa akmed \n")


print("beberapa hari kemudian tanpa disengaja fatikh dan akhmed bertemu di jalan.\n")

print(f"{orangkedua} :eh {orangpertama},ketemu lagi nih. kamu sekarang kuliah di universitas trunojoyo ? iya/tidak ")
jawaban_1 = input(f"{orangpertama} : ")

if jawaban_1.lower() == "iya" :
    print(f"{orangkedua} : oh sama kita")
else:
    print(f"{orangkedua} : tidak salah lagi kan maksudnya")
    
print(f"{orangpertama} : yaaa begitulah")
print(f"{orangkedua} : gk nyangka banget satu univ haha. oh iya sekarang kamu dikelas mana ? rkbf lantai 2/rkbf lantai 3")
jawaban_2 = input(f"{orangpertama} : ")

if jawaban_2 == kelas2 :
    print(f"{orangkedua} : oh kita kelas kita sama")
else:
    print(f"{orangkedua} : yah ku kira kelas kita sama")

print(f"{orangpertama} : yaudah ayok kita jalan ke kelas aja")
print(f"{orangkedua} : yaudah yokk")
print(f"{orangpertama} : oh iya nanti mau gk kerumah aku pulang pelajaran nanti")
print(f"{orangkedua} : iya nanti kita janjin digerbang depan ya")
print("fatikh dan akhmed pun bertemu digerbang dan pulng bersama\n")


print(f"dijalan {orangpertama} dan {orangkedua} membeli es\n")
print(f"{orangpertama} : {orangkedua}, yuk beli se dulu")
print(f"{orangkedua} : yuk")

esteh_fatikh = int(input(f"{orangpertama} : aku beli "))
esteh_akhmed = int(input(f"{orangkedua} : aku "))

hasil_esteh = abs(esteh_fatikh + esteh_akhmed)

print(f"{orangpertama} : kan {orangkedua} beli {esteh_akhmed}, kalo aku kan beli {esteh_fatikh}, jadi totalnya {hasil_esteh} ")
print(f"{orangkedua} : okeyy\n")

print(f"sehabis beli esteh {orangpertama} dan {orangkedua} pun melanjutkan perjalanan sampai kerumah {orangpertama}\n")
print(f"{orangpertama} :ayo masuk med")
print(f"{orangkedua} :iya makasih tikh assalamualaikum?")
print(f"{orangpertama} :waalaikumsallam.eh kita langsung kekamar aku aja")
print(f"{orangkedua} :ayo.ngomong ngomong rumah kamu kayak masih berantakan ya")

print(f"{orangpertama} :kan aku baru pindah med")
print(f"{orangkedua} :oh iya ya aku lupa hehehe")

print("setelah berbincang bincang sampai malam akhmed pun pulang kerumahnyaa")
print("sekian cerita saya terima kasih.tamat")