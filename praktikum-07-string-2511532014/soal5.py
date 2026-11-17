# Name: Haykal Muhammad Dahnil
# NIM: 2511532014
# Question 5

# Bagian A
"""

username = input("Username: ")

if len(username) < 5:
    print("Invalid: at least 5 character")
elif not username.isalnum():
    print("Invalid: letters and digits only")
elif username[0].isdigit():
    print("Invalid: must start with a letter")
else:
    print("Valid")

"""

# Bagian B

nim = input("Masukkan NIM: ")

if len(nim) == 10 and nim.isdigit():
    intake = "20" + nim[:2]
    print("Valid")
    print(f"Intake year {intake}")
else:
    print("Invalid NIM")