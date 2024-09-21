hargataserika= 45.000
hargatassaskia = 55.000


 # Input nama pengguna
nama1 = input("hallo dengan siapa ini?")
print("hallo" , nama1 , "salam kenal")

print("mari kita baca obrolan erika dan saskia")

input("masukkan angka 1 untuk next chapter ")
# Percakapan dimulai
print("erika: eh haloo saskia, tadi aku liat kamu beli tas yang sama seperti tasku di toko depan sana harganya berapa sih?")
print("saskia: haloo jugaa erika! tasku harganya" , hargatassaskia , "harga tasmu berapa er?")
print("erika: harga tasku sii" , hargataserika , "sas.")

 # Operasi aritmatika
selisihharga = hargatassaskia - hargataserika
print("erika: loh kok beda ya harganya padahal modelnya sama, berarti harga tas kita" , selisihharga , "ya.")

# Input dari pengguna
tebakanharga = int(input(" coba tebak berapa selisih harga tas erika dan saskia: "))

# Operasi aritmatika dan logika
selisihharga = hargataserika - hargatassaskia

# Output hasil tebakan
if tebakanharga == 10.000 :
    print("erika: Wah benar bangett!")
else :
    print("sakia: Maaf yaa, tebakanmu salah. selisih harga dari tas kami sebenarnya" , selisihharga , "lho.")

input("tekkan angka 1 untuk melanjutkan dialog")

# # Pertanyaan tambahan dengan operasi logika
print("erika: Hei saskia, aku punya pertanyaan matematika nihh buat kamu.")
erika_number = 14
saskia_number = 11
    
print("erika: Jika aku punya" , {erika_number} , "lolipop dan kamu punya" , {saskia_number} , "lolipop, berapa total lolipop kita?")
    
user_answer = int(input("coba bantu saskia menjawab: "))

hasil = erika_number + saskia_number

if user_answer == hasil :
        print("saskia: Terimakasih sudah menjawab, Jawabannya benar.")
else :
        print("saskia: Hmm, sepertinya itu jawaban kamu kurang tepat. Jumlah yang benar adalah" , hasil ,"lolipop")

# Akhir percakapan
print("erika: Terima kasih yaa saskia sudah mengobrol")
print("saskia: Sama-sama, Reva. Dan terima kasih juga untuk" , nama1 ," yang sudah berpartisipasi!")