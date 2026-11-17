# Name: Haykal Muhammad Dahnil
# NIM: 2511532014
# Question 4

phone = "082511532014"
masked = phone[:4] + "*" * len(phone[4:-3]) + phone[-3:]
print(masked)
