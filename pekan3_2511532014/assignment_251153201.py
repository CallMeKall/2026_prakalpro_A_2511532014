angka1_2014 = int(input("Input angka-1: " ))
angka2_2014 = int(input("Input angka-2: " ))

print("\nNilai awal angka1 = ", angka1_2014)
print("Nilai awal angka2 = ", angka2_2014)

# assignment biasa
hasil_2014 = angka1_2014
print("\nassignment biasa (=)")
print("hasil = ", hasil_2014)

# assignment penjumlahan
hasil_2014 = angka1_2014
hasil_2014 += angka2_2014
print("\nassignment penambahan (+=)")  
print("hasil = ", hasil_2014)

# assignment pengurangan
hasil_2014 = angka1_2014
hasil_2014 -= angka2_2014
print("\nassignment pengurangan (-=)")
print("hasil = ", hasil_2014)

# assignment perkalian
hasil_2014 = angka1_2014
hasil_2014 *= angka2_2014
print("\nassignment perkalian (*=)")
print("hasil = ", hasil_2014)

# assignment pembagian, pembagian bulat dan sisa bagi
if angka2_2014 != 0:
    hasil_2014 = angka1_2014
    hasil_2014 /= angka2_2014
    print("\nassignment pembagian (/=)")
    print("hasil = ", hasil_2014)

    hasil_2014 = angka1_2014
    hasil_2014 //= angka2_2014
    print("\nassignment pembagian bulat (//=)")
    print("hasil = ", hasil_2014)

    hasil_2014 = angka1_2014
    hasil_2014 %= angka2_2014
    print("\nassignment sisa bagi (%=)")
    print("hasil = ", hasil_2014)
else :
    print("\nPembagian tidak dapat dilakukan!")
    print("Angka kedua tidak boleh bernilai 0!")

# Operator tambahan: assignment perpangkatan
hasil_2014 = angka1_2014
hasil_2014 **= angka2_2014
print("\nassignment perpangkatan (**=)")
print("hasil = ", hasil_2014)