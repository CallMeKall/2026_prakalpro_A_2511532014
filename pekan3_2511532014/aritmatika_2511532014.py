angka1_2014 = int(input("Input angka-1: " ))
angka2_2014 = int(input("Input angka-2: " ))

#Penjumlahan
hasil_2014 = angka1_2014 + angka2_2014
print("\nOperator penjumlahan")
print("Hasil", hasil_2014)

# Pengurangan
hasil_2014 = angka1_2014 - angka2_2014  
print("\nOperator pengurangan")
print("Hasil", hasil_2014)

# Perkalian
hasil_2014 = angka1_2014 * angka2_2014
print("\nOperator perkalian")
print("Hasil", hasil_2014)

# Pembagian, pembagian bulat dan sisa bagi
if angka2_2014 != 0:

    hasil_2014 = angka1_2014 / angka2_2014
    print("\nOperator pembagian")
    print("Hasil", hasil_2014)

    hasil_2014 = angka1_2014 // angka2_2014
    print("\nOperator pembagian bulat")
    print("Hasil", hasil_2014)

    hasil_2014 = angka1_2014 % angka2_2014
    print("\nOperator sisa bagi")
    print("Hasil", hasil_2014)

else :
    print("Angkat kedua tidak boleh bernilai 0!")

# Pangkat
hasil_2014 = angka1_2014 ** angka2_2014
print("\nOperator pangkat")
print("Hasil", hasil_2014)