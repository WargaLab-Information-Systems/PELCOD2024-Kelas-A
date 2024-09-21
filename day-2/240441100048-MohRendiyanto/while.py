#ini adalah perulangan while
name = input ("masukan nama anda")

while name == "":
    print("masukan ulang nama anda")
    nama = input ("masukan nama anda : ")

print(f"hallo guys {nama}")

#ini adalah perulangan while not
nama = input("masukan nama anda : ")
while not name.lower () == "k":
    print("masukan ulang nama anda")
    nama = input ("masukan nama anda : ")

print(f"byee byee")
