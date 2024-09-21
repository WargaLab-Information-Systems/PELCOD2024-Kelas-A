nama1 = "Rendy"
nama2 = "kak suci"

print(f"{nama1} : hallo,{nama2} lagi ngapain nihh")
print(f"{nama2} : ehh dek {nama1} ya ga ngapa-ngapain si, cuma lagi nyantai aja sambil nunggu matkul abis ini, sini duduk dek {nama1}")
print(f"{nama1} : iyaa kak")
print(f"{nama1} : aku mau nanya boleh ga kak?")
print(f"{nama2} : bolee, mau nanya apa nihhh.")
print(f"{nama1} : aku tadi tu abis nasi sama lauknya diwarung prasmanan, nah semuanya itu jdi 15 ribu ada tiga macem lauk, ada ayam,tempe dan udang. padahal kemaren aku beli pake ayam sama tempe cuma 11 ribu kak. Berarti kalo nambah udang harus nambah berapa ya kak.")
print(f"{nama2} : kalo kemaren pas kamu beli ayam sama tempe 11 ribu,dan tadi kamu beli ayam,tempe,dan udang 15 ribu berarti semuanya itu")
jawaban = int(input(f"{nama2} :"))

hasil = 11 + 4 
if hasil == jawaban:
    print(f"{nama2} :berarti udangnya itu 4 ribu dek")
    print(f"{nama1} :oh iya ya kak, mahal juga ya ternyata")
else:
    print(f"{nama2} :eh ga tau deh, aku ga per nah beli disana soalnya")
    print(f"{nama1} :iya deh kak nanti aku tanya dulu aja sebelum beli")