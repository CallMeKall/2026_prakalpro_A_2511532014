a1_2014 = input("Input nilai boolean-1 (True/False): " ).strip().lower() == "true"
a2_2014 = input("Input nilai boolean-2 (True/False): " ).strip().lower() == "true"

print("\nA1 = ", a1_2014)
print("A2 = ", a2_2014)

#konjungsi: bernilai Truew jika keduanya true
hasil_2014 = a1_2014 and a2_2014
print("\nOperator konjungsi (and)")
print("A1 and A2 = ", hasil_2014)

#disjungsi: bernilai True jika salah satu true
hasil_2014 = a1_2014 or a2_2014
print("\nOperator disjungsi (or)")
print("A1 or A2 = ", hasil_2014)

#negasi A1: membalik nilai A1
hasil_2014 = not a1_2014
print("\nOperator negasi A1 (not)")
print("not A1 = ", hasil_2014)

#negasi A2: membalik nilai A2
hasil_2014 = not a2_2014
print("\nOperator negasi A2 (not)")
print("not A2 = ", hasil_2014)

#Xor: bernilai true jika kedua nilai berbeda
hasil_2014 = a1_2014 != a2_2014
print("\nOperator Xor (xor)")
print("A1 xor A2 = ", hasil_2014)