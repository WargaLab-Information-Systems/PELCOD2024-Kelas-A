def hitung_kata(kalimat):
    kata_list = kalimat.split()
    return len(kata_list)

while true:
    kalimat = input("masukan sebuah kalimat (atau ketik k untuk keluar) : ")

    if kalimat.lower() == "k":
        print("terimakasih telah menghitung kata disini")
        break

    jumlah_kata = hitung_kata(kalimat)
    print(f"jumlah kata dalam kalimat adalah {jumlah_kata}")
