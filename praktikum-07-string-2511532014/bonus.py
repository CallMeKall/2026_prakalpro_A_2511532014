# Name: Haykal Muhammad Dahnil
# NIM: 2511532014
# Question Bonus

kalimat = input("Input kalimat: ")

temp = kalimat.replace(" ", "").lower()
balik = temp[::-1]

if temp == balik:
    print("Palindrome")
else:
    print("Not a palindrome")