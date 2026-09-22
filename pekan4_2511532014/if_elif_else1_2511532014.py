umur_2014 = int(input("Input umur anda: "))
sim_2014 = input("Apakah anda sudah punya SIM C (y/t): ")[0]

if umur_2014 >= 17 and sim_2014 == 'y':
    print("Anda sudah dewasa dan sudah boleh bawa motor")
elif umur_2014 >= 17 and sim_2014 != 'y':
    print("Anda sudah dewasa tetapi tidak boleh bawa motor")
elif umur_2014 < 17 and sim_2014 == 'y':
    print("Anda belum cukup umur untuk punya SIM")
else:
    print("Anda belum cukup umur untuk bawa motor")
print("Program Selesai")