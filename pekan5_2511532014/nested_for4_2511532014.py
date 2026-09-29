tinggi_2014 = int(input("Masukkan tinggi pola (bilangan genap): "))

if tinggi_2014 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_2014 = tinggi_2014
    c_2014 = a_2014
    lebar_2014 = (2 * tinggi_2014) - 2

    for i_2014 in range(1, tinggi_2014 + 1):
        b_2014 = c_2014 + 1

        for j_2014 in range(1, lebar_2014 + 1):

            if i_2014 == 1 or i_2014 == tinggi_2014:
                if j_2014 == 1 or j_2014 == lebar_2014:
                    print("#", end="")
                else:
                    print("=", end="") 
            else:
                if j_2014 == 1 or j_2014 == lebar_2014:
                    print("|", end="")
                else:
                    if j_2014 == c_2014:
                        print("<", end="")
                    elif j_2014 == b_2014:
                        print(">", end="")
                    elif j_2014 == (lebar_2014 - c_2014):
                        print("<", end="")
                    elif j_2014 == (lebar_2014 - c_2014 + 1):
                        print(">", end="")
                    elif j_2014 > b_2014 and j_2014 < (lebar_2014 - c_2014):
                        print(".", end="")
                    else:
                        print(" ", end="")

        print()

        a_2014 -= 2

        if a_2014 <= 0:
            c_2014 = (-a_2014) + 2
        else:
            c_2014 = a_2014