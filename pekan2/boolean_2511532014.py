is_Lulus_2014 = True
is_cumlaude = True

# menggunakan boolean
nilai_2014 = 85
batas_lulus_2014 = 75

#menenutkan nilain boolean darin kondisi
status_kelulusan_2014 = nilai_2014 >= batas_lulus_2014 #hasilnya akan true

print("=== Check Kelulusan ===")
print("Nilai: ", nilai_2014)
print("Apakah siswa lulus?:", status_kelulusan_2014)
if is_Lulus_2014 and is_cumlaude:
    print("Selamat anda lulus dengan predikat Cum Laude!")