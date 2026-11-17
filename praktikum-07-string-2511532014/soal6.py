# Name: Haykal Muhammad Dahnil
# NIM: 2511532014
# Question 6

full_name = "Haykal Muhammad Dahnil"
nim = "2511532014"

nama_bersih = full_name.strip()
posisi_spasi = nama_bersih.find(" ")

if posisi_spasi == -1:
    nama_depan = nama_bersih
else:
    nama_depan = nama_bersih[:posisi_spasi]

username = nama_depan.lower() + nim[-3:]
print(username)