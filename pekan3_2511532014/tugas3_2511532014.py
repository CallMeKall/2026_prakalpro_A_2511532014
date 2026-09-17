

print("==========================================")
print("       SISTEM TRANSAKSI TOKO")
print("==========================================")


nama_2014 = input("Masukkan Nama Pelanggan : ")
status_2014 = input("Masukkan Status Pelanggan (member/nonmember) : ")
total_belanja_2014 = int(input("Masukkan Total Belanja : "))
jumlah_barang_2014 = int(input("Masukkan Jumlah Barang : "))
kode_promo_2014 = input("Masukkan Kode Promo : ").upper()


belanja_minimum_2014 = total_belanja_2014 >= 200000
jumlah_minimum_2014 = jumlah_barang_2014 >= 3
status_member_2014 = status_2014 == "member"

daftar_promo_2014 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]

promo_tersedia_2014 = kode_promo_2014 in daftar_promo_2014
promo_tidak_tersedia_2014 = kode_promo_2014 not in daftar_promo_2014

diskon_member_2014 = status_member_2014 and belanja_minimum_2014

promo_2014 = jumlah_minimum_2014 or promo_tersedia_2014

promo_invalid_2014 = not promo_tersedia_2014

# operator aritmatika
diskon_2014 = 0

if diskon_member_2014:
    diskon_2014 = total_belanja_2014 * 10 / 100

total_pembayaran_2014 = total_belanja_2014 - diskon_2014

rata_rata_2014 = total_belanja_2014 / jumlah_barang_2014

# Operator modulus (%)
sisa_bagi_2014 = total_belanja_2014 % jumlah_barang_2014

poin_2014 = 0

if status_member_2014:
    poin_2014 += 10

if promo_tersedia_2014:
    poin_2014 += 5

jumlah_barang_setelah_2014 = jumlah_barang_2014
if jumlah_barang_setelah_2014 > 0:
    jumlah_barang_setelah_2014 -= 1

# Membandingkan identitas objek
status_asli_2014 = status_2014
status_baru_2014 = str(status_2014)

identity_sama_2014 = status_asli_2014 is status_baru_2014
identity_berbeda_2014 = status_asli_2014 is not status_baru_2014

nilai_sama_2014 = status_asli_2014 == status_baru_2014
"""""
bitwise
Nilai bit:
0001 = Member
0010 = Belanja >= 200000
0100 = Jumlah barang >= 3
1000 = Promo tersedia
"""""

kode_member_2014 = 1       # 0001
kode_belanja_2014 = 2      # 0010
kode_barang_2014 = 4       # 0100
kode_promo_bit_2014 = 8    # 1000

kode_status_2014 = 0

if status_member_2014:
    kode_status_2014 = kode_status_2014 | kode_member_2014

if belanja_minimum_2014:
    kode_status_2014 = kode_status_2014 | kode_belanja_2014

if jumlah_minimum_2014:
    kode_status_2014 = kode_status_2014 | kode_barang_2014

if promo_tersedia_2014:
    kode_status_2014 = kode_status_2014 | kode_promo_bit_2014


# Operator AND (&)
cek_member_2014 = kode_status_2014 & kode_member_2014
cek_promo_bit_2014 = kode_status_2014 & kode_promo_bit_2014

# Operator OR (|)
kode_gabungan_2014 = kode_status_2014 | kode_member_2014

# Operator XOR (^)
kode_referensi_2014 = 11       # 1011
perbedaan_status_2014 = kode_status_2014 ^ kode_referensi_2014

# Operator shift
kode_shift_2014 = kode_status_2014 << 1


#Hak akses pelanggan

member_access_2014 = cek_member_2014 == kode_member_2014
promo_access_2014 = cek_promo_bit_2014 == kode_promo_bit_2014

free_shipping_access_2014 = (
    promo_tersedia_2014 and
    kode_promo_2014 == "GRATISONGKIR"
)

# Output Data Pelanggan

print("\n==========================================")
print("             DATA PELANGGAN")
print("==========================================")

print("Nama Pelanggan       :", nama_2014)
print("Status Pelanggan     :", status_2014)
print("Total Belanja        : Rp", total_belanja_2014)
print("Jumlah Barang        :", jumlah_barang_2014)
print("Kode Promo           :", kode_promo_2014)

#output validasi
print("\n==========================================")
print("             HASIL VALIDASI")
print("==========================================")

print("Belanja >= Rp200000       :", belanja_minimum_2014)
print("Jumlah Barang >= 3        :", jumlah_minimum_2014)
print("Status Member             :", status_member_2014)
print("Kode Promo Tersedia       :", promo_tersedia_2014)
print("Kode Promo Tidak Tersedia :", promo_tidak_tersedia_2014)
print("Mendapatkan Diskon        :", diskon_member_2014)
print("Mendapatkan Promo         :", promo_2014)

#output perhitungan
print("\n==========================================")
print("            HASIL PERHITUNGAN")
print("==========================================")

print("Diskon                   : Rp", int(diskon_2014))
print("Total Pembayaran         : Rp", int(total_pembayaran_2014))
print("Rata-rata Harga Barang   : Rp", int(rata_rata_2014))
print("Sisa Pembagian (%)       :", sisa_bagi_2014)
print("Poin Pelanggan           :", poin_2014)

#output hak akses
print("\n==========================================")
print("          HAK AKSES PELANGGAN")
print("==========================================")

print("Kode Hak Akses           :", kode_status_2014)
print("Member Access            :", member_access_2014)
print("Promo Access             :", promo_access_2014)
print("Free Shipping Access     :", free_shipping_access_2014)

#output operator identity
print("\n==========================================")
print("          OPERATOR IDENTITY")
print("==========================================")

print("status_asli is status_baru     :", identity_sama_2014)
print("status_asli is not status_baru :", identity_berbeda_2014)
print("status_asli == status_baru     :", nilai_sama_2014)

#Output operasi bitwise
print("\n==========================================")
print("            OPERASI BITWISE")
print("==========================================")

print("Kode Status Transaksi")
print("0001 | 0010 | 0100 | 1000")

print("Kode Biner   :", format(kode_status_2014, "04b"))
print("Kode Desimal :", kode_status_2014)

print("\n--- Pemeriksaan Status Member ---")
print(format(kode_status_2014, "04b"),
      "&",
      format(kode_member_2014, "04b"))

print("Hasil Biner   :", format(cek_member_2014, "04b"))
print("Hasil Desimal :", cek_member_2014)

print("\n--- Pemeriksaan Status Promo ---")
print(format(kode_status_2014, "04b"),
      "&",
      format(kode_promo_bit_2014, "04b"))

print("Hasil Biner   :", format(cek_promo_bit_2014, "04b"))
print("Hasil Desimal :", cek_promo_bit_2014)

print("\n--- Operator OR ---")
print(format(kode_status_2014, "04b"),
      "|",
      format(kode_member_2014, "04b"))

print("Hasil Biner   :", format(kode_gabungan_2014, "04b"))
print("Hasil Desimal :", kode_gabungan_2014)

print("\n--- Perbandingan Status XOR ---")
print("Kode Transaksi :", format(kode_status_2014, "04b"))
print("Kode Referensi :", format(kode_referensi_2014, "04b"))

print(format(kode_status_2014, "04b"),
      "^",
      format(kode_referensi_2014, "04b"))

print("Hasil Biner   :", format(perbedaan_status_2014, "04b"))
print("Hasil Desimal :", perbedaan_status_2014)

print("\n--- Operator Shift ---")
print(format(kode_status_2014, "04b"), "<< 1")

print("Hasil Biner   :", format(kode_shift_2014, "05b"))
print("Hasil Desimal :", kode_shift_2014)

print("\n==========================================")
print("              SELESAI")
print("==========================================")