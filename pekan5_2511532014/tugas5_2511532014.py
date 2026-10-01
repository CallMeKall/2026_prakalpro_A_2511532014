print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")

n_1234 = int(input("Masukkan ukuran skala jam pasir (N): "))

for pagar_1234 in range(1):
    print("#", end="")
    for sama_1234 in range(4 * n_1234 + 5):
        print("=", end="")
    print("#")

for baris_1234 in range(n_1234, 0, -1):
    print("|", end="")
    print(" ", end="")

    for spasi_1234 in range(2 * (n_1234 - baris_1234)):
        print(" ", end="")

    for angka_1234 in range(baris_1234, 0, -1):
        print(angka_1234, end=" ")
    
    print("<*>", end="")

    for angka_1234 in range(1, baris_1234 + 1):
        print(" ", end="")
        print(angka_1234, end="")

    for spasi_1234 in range(2 * (n_1234 - baris_1234)):
        print(" ", end="")

    print(" |")

print("|", end="")
for spasi_1234 in range(2 * n_1234 + 1):
    print(" ", end="")
print("<*>", end="")
for spasi_1234 in range(2 * n_1234 + 1):
    print(" ", end="")
print("|")

for baris_1234 in range(1, n_1234 + 1):
    print("|", end="")
    print(" ", end="")

    for spasi_1234 in range(2 * (n_1234 - baris_1234)):
        print(" ", end="")

    for angka_1234 in range(baris_1234, 0, -1):
        print(angka_1234, end=" ")

    print("<*>", end="")

    for angka_1234 in range(1, baris_1234 + 1):
        print(" ", end="")
        print(angka_1234, end="")

    for spasi_1234 in range(2 * (n_1234 - baris_1234)):
        print(" ", end="")

    print(" |")

for pagar_1234 in range(1):
    print("#", end="")
    for sama_1234 in range(4 * n_1234 + 5):
        print("=", end="")
    print("#")