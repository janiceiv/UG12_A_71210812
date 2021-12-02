kata = input("Input : ")

print("Output : ")
pjgkata = len(kata)

for tinggi in range(pjgkata):
    for baris in range(tinggi + 1):
        print(kata[baris], end="")
    print()


