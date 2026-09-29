batas_2014 = int(input("Masukkan nilai batas: "))
for line_2014 in range(1, batas_2014 + 1):
    for j_2014 in range(1, (-1* line_2014 + batas_2014) + 1):
        print(".", end="")
    print(line_2014)