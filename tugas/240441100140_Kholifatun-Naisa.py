print("Raisa: Halo! Nuri apa kabar?")
print("Nuri: Baik..")
print("Raisa: Apakah kamu sudah menjalani ujian akhir?")
print("Nuri: sudah, baru selesai kemarin")
print("Nuri: Kamu sudah selesai taa?")
print("Raisa: baru selesai hari ini")
print("Nuri: oalahh")
print("Raisa: Kamu lagi ngapain?")
print("Nuri: Aku lagi cek nilai ujian Bahasa Inggris dan Bahasa Indonesia ku nihh")
print("Raisa: Btw, itu gimana cara ngeceknya?")
print("Nuri: sekolah kita kan menyediakan aplikasinya.")
print("Raisa: Ohh iya, gimana tuh caranya?")
input_nama = input("Nuri: Gini, nih, pertama kamu masukkan namamu terlebih dahulu, sini tak bantu. Namamu siapa? ")

print ("KOMPUTER")
nilai_inggris = int(input(f"{input_nama}, berapa nilai Bahasa Inggrismu? "))
nilai_indonesia = int(input(f"{input_nama}, berapa nilai Bahasa Indonesiamu? "))

def APK():
    print(f"\n{input_nama}, anda penasaran dengan nilai Bahasa Inggris dan Bahasa Indonesiamu.")
    
    print("\nSilahkan pilih operasi yang tersedia:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    
    pilihan = input("\nAnda memili operasi: ")

    if pilihan == '1':
        hasil = nilai_inggris + nilai_indonesia
        print(f"Hasil penjumlahan {nilai_inggris} + {nilai_indonesia} = {hasil}")
    elif pilihan == '2':
        hasil = nilai_inggris - nilai_indonesia
        print(f"Hasil pengurangan {nilai_inggris} - {nilai_indonesia} = {hasil}")
    elif pilihan == '3':
        hasil = nilai_inggris * nilai_indonesia
        print(f"Hasil perkalian {nilai_inggris} * {nilai_indonesia} = {hasil}")
    elif pilihan == '4':
        hasil = nilai_inggris / nilai_indonesia if nilai_indonesia != 0 else "Pembagian dengan 0 tidak diperbolehkan!"
        print(f"Hasil pembagian {nilai_inggris} / {nilai_indonesia} = {hasil}")
    else:
        print("Pilihan operasi tidak valid.")
    
    print("Nuri: gimana, gampang banget kann?")
    print("Raisa: iyaa nihh")
    print("Nuri: kita harus menafaatkan fasilitas yang dimiliki oleh sekolah")
    print("Raisa: hahaha.. iyaa")
    print("Nuri: yasudah kalo gituaku balik ke kelas dulu yaa")
    print("Raisa: ohh okeee terimakasih yaaa")

# Memulai percakapan aritmatika
APK()
