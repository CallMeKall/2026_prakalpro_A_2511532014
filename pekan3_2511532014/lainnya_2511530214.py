print("=======================")
print("1. Operator Keanggotaan")
print("=======================")

#input beberapa data yang dipisahkan dengan koma
input_data_2014 = input("Masukan beberapa angka, pisahkan dengan koma: " )

# mengubah input menjadi list integer
data_2014 = [int(angka.strip()) for angka in input_data_2014.split(",")]

nilai_dicari_2014 = int(input("Masukan angka yang ingin dicari: " ))

# operator in
hasil_2014 = nilai_dicari_2014 in data_2014
print("\nOperator Keanggotan IN")
print(nilai_dicari_2014,"in", data_2014, "=", hasil_2014)

# operator not in
hasil_2014 = nilai_dicari_2014 not in data_2014
print("\nOperator Keanggotan NOT IN")
print(nilai_dicari_2014,"not in", data_2014, "=", hasil_2014)

print("=======================")
print("2. Operator Identitas")
print("=======================")

# objek1 menggunakan list dari input pengguna
objek1_2014 = data_2014

# objek2 merujuk pada objek yang sama dengan objek1
objek2_2014 = objek1_2014

# objek3 memiliki isi sama, tetapi merupakan objek baru
objek3_2014 = data_2014.copy()

print("objek1 =", objek1_2014)
print("objek2 =", objek2_2014)
print("objek3 =", objek3_2014)

# operator is
hasil_2014 = objek1_2014 is objek2_2014
print("\nOperator Identitas IS")
print("objek1 is objek2 =", hasil_2014)

# operatoris not
hasil_2014 = objek1_2014 is not objek3_2014
print("\nOperator Identitas IS NOT")    
print("objek1 is not objek3 =", hasil_2014)

# membandingkan identitas dan nilai
print("\nMembandingkan identitas dan nilai")
print("objek1 is objek3 =", objek1_2014 is objek3_2014)
print("objek1 == objek3 =", objek1_2014 == objek3_2014)
