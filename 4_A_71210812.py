angka = int(input("Input : "))
a = 2
print("Output : ")

for tinggi in range(1,1+angka):
    for baris in range(1,2*angka):
        if tinggi + baris == angka+ 1 or baris - tinggi == angka - 1:
            print("*", end="")
        elif tinggi == angka and baris != a:
            print("*", end="")
            a = a + 2
        else:
            print(end=" ")
    print()
