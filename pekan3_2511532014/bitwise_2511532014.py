print("=======================")
print("  3. Operator Bitwise")
print("=======================")

angka1_2014 = int(input("Input angka bitwise-1: " ))
angka2_2014 = int(input("Input angka bitwise-2: " ))

print("\nAngka dalam bentuk desimal dan biner")
print("Angka 1: ", angka1_2014, "| Biner: ", bin(angka1_2014))
print("Angka 2: ", angka2_2014, "| Biner: ", bin(angka2_2014))

# bitwise and
hasil_2014 = angka1_2014 & angka2_2014
print("\nbitwise AND (&)")
print(angka1_2014, "&", angka2_2014, "=", hasil_2014,)
print("Biner hasil = ", bin(hasil_2014))
print("Biner hasil (8 bit) = ", format(hasil_2014, '08b'))

# bitwise OR
hasil_2014 = angka1_2014 | angka2_2014
print("\nbitwise OR (|)")
print(angka1_2014, "|", angka2_2014, "=", hasil_2014,)
print("Biner hasil = ", bin(hasil_2014))
print("Biner hasil (8 bit) = ", format(hasil_2014, '08b'))

# bitwise xor
hasil_2014 = angka1_2014 ^ angka2_2014
print("\nbitwise XOR (^)")
print(angka1_2014, "^", angka2_2014, "=", hasil_2014,)
print("Biner hasil = ", bin(hasil_2014))
print("Biner hasil (8 bit) = ", format(hasil_2014, '08b'))

# bitwise not
hasil_2014 = ~angka1_2014
print("\nbitwise NOT (~)")
print("~", angka1_2014, "=", hasil_2014)
print("Biner hasil = ", bin(hasil_2014))
print("Biner hasil (8 bit) = ", format(hasil_2014, '08b'))

# bitwise geser kiri
jumlah_geser_2014 = int(input("\nMasukan jumlah pergeseran bit: "))

hasil_2014 = angka1_2014 << jumlah_geser_2014
print("\nbitwise geser kiri (<<)")
print(angka1_2014, "<<", jumlah_geser_2014, "=", hasil_2014)
print("Biner hasil = ", bin(hasil_2014))
print("Biner hasil (8 bit) = ", format(hasil_2014, '08b'))

# bitwise geser kanan
hasil_2014 = angka1_2014 >> jumlah_geser_2014
print("\nbitwise geser kanan (>>)")
print(angka1_2014, ">>", jumlah_geser_2014, "=", hasil_2014)
print("Biner hasil = ", bin(hasil_2014))
print("Biner hasil (8 bit) = ", format(hasil_2014, '08b'))