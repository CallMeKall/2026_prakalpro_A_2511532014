ulang_2014 = int(input("Masukkan jumlah perulangan: "))

jumlah_2014 = 0
for i_2014 in range(1, ulang_2014 + 1):
    print(i_2014, end=" ")
    jumlah_2014 = jumlah_2014 + 1

    if i_2014 < ulang_2014:
        print(" + ", end="")
    else:
        print(" = ", jumlah_2014, end="")
print()
print("Jumlah = ", jumlah_2014)