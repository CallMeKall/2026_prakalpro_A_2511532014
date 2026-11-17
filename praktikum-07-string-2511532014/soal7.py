# Name: Haykal Muhammad Dahnil
# NIM: 2511532014
# Question 7

nama = "haykal muhammad dahnil"
nim = "2511532014"


nama_bersih = nama.strip()
posisi_spasi = nama_bersih.find(" ")
intake = "20" + nim[:2]

if posisi_spasi == -1:
    nama_depan = nama_bersih
else:
    nama_depan = nama_bersih[:posisi_spasi]

username = nama_depan.lower() + nim[-3:]

print("==============================")
print("         STUDENT CARD         ")
print("==============================")
print("Name      : " + nama.title())
print("NIM       : " + nim)
print("Username  : " + username)
print("Intake    : " + intake)
print("==============================")
