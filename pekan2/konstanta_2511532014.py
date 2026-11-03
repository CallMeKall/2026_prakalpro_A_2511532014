from typing import Final
PI_2014: Final = 3.14
print("pi: %f" % (PI_2014))
jari_2014 = float(input("Masukan jari-jari lingkaran: "))
luas_2014 = PI_2014 * jari_2014 * jari_2014
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_2014, luas_2014))