nama = input("Masukkan Nama : ")
kursi = int(input("Masukkan nomor kursi " + str(nama) + ": "))
list1 = []

if kursi in list1:
        print("Mohon maaf kursi tersebut telah terisi")
else:
    nama = input("Masukkan Nama : ")

    
while (nama != "STOP"):
    kursi = int(input("Masukkan nomor kursi " + str(nama) + ": "))
    list1.append(kursi)
    nama = input("Masukkan Nama : ")

  
print("List kursi yang telah terisi :")
print("Kursi nomor", kursi, "telah diisi oleh", nama)
