tinggi_2014 = int(input("Masukkan tinggi segitga: "))

for i_2014 in range(1, tinggi_2014 + 1):
    for j_2014 in range(tinggi_2014 - i_2014):
        print(" ", end="")
    for k_2014 in range(i_2014):
        print("*", end=" ")
    print()