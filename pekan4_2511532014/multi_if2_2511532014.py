#input dari user
total_belanja_2014 = float(input("Masukkan total belanja (Rp): "))

#input status member (mengecek apakah user mengetik y atau ya)
input_member_2014 = input("Apakah anda member? (y/t): ").strip().lower()
is_member_2014 = input_member_2014 in ["y", "ya"]

# input status kode promo
input_promo_2014 = input("Apakah kode promo valid? (y/t): ").strip().lower()
kode_promo_valid_2014 = input_promo_2014 in ["y", "ya"]

total_diskon_persen_2014 = 0

# multi if terpisah: setiap kondisi diperiksa secara independen
# diskon bisa ditumpuk (akumulasi) jika memenuhi beberapa syarat sekaligus

if total_belanja_2014 > 1000000:
    total_diskon_persen_2014 += 10

if is_member_2014:
    total_diskon_persen_2014 += 5

if kode_promo_valid_2014:
    total_diskon_persen_2014 += 15

#  menghitung nominal diskon dan total bayar
nominal_diskon_2014 = total_belanja_2014 * (total_diskon_persen_2014 / 100)
total_bayar_2014 = total_belanja_2014 - nominal_diskon_2014


# output hasil
print("\n--- Rincian Pembayaran ---")
print(f"Total Diskon  : {total_diskon_persen_2014}% (Rp {nominal_diskon_2014:,.0f})")
print(f"Total Bayar   : Rp {total_bayar_2014:,.0f}")

print(f"Total diskon yang anda dapatkan : {total_diskon_persen_2014}%")
# output: Total diskon yang anda dapatkan: 30% jika belanja > 1jt, member dan kode promo valis