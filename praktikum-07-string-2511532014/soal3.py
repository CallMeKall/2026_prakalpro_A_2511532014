# Name: Haykal Muhammad Dahnil
# NIM: 2511532014
# Question 3

text = "Informatika"
print(text[-1])
print(text.upper)
print(text[0:20])

text = "Haykal Muhammad Dahnil"
count = 0
for char in text:
    if char in "aiueoAIUEO":
        count += 1
print("Vowels:", count)
