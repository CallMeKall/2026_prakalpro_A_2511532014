from typing import Final
PI: Final = 3.14
print("pi: %f" % (PI))
jari_2014 = float(input("Masukan jari-jari lingkaran: "))
luas_2014 = PI * jari_2014 * jari_2014
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_2014, luas_2014))