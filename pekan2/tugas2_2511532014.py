from typing import Final

BATAS_LULUS: Final = 75.0

# Input
nama_2014 = input("Masukkan Nama Mahasiswa : ")
jenis_kelamin_2014 = input("Masukkan Jenis Kelamin (L/P): ")
umur_2014 = int(input("Masukkan Umur : "))
nilai_2014 = float(input("Masukkan Skor Tes Awal : "))

alamat_2014 = """Pasa Ambacang,
Pauh,
Kota Padang"""

token_2014 = 100 + 3j

lulus_2014 = nilai_2014 >= BATAS_LULUS

# Output
print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
print("Nama Mahasiswa :", nama_2014, "| Tipe:", type(nama_2014))
print("Jenis Kelamin :", jenis_kelamin_2014, "| Tipe:", type(jenis_kelamin_2014))
print("Alamat Domisili:")
print(alamat_2014, "| Tipe:", type(alamat_2014))
print("Umur :", umur_2014, "tahun | Tipe:", type(umur_2014))
print("Skor Tes Awal :", nilai_2014, "| Tipe:", type(nilai_2014))
print("ID Token Sinyal:", token_2014, "| Tipe:", type(token_2014))

print("\n=== STATUS KELULUSAN PRAKTIKUM ===")
print("Batas Minimum Nilai:", BATAS_LULUS)
print("Apakah Dinyatakan Lulus?:", lulus_2014, "| Tipe:", type(lulus_2014))