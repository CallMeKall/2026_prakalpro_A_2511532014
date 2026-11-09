PASS_SCORE = 65

number_of_students = int(input("Number of students: "))
while number_of_students <= 0:
    print("Invalid Student count")
    number_of_students = int(input("Number of students: "))

passed = 0
total = 0
lowest = 101

for i in range(1, number_of_students + 1):
    print("Student", i)

    score = int(input("Enter score: "))

    while score < 0 or score > 100:
        print("Invalid score!")
        score = int(input("Enter score: "))
    total += score

    if score >= PASS_SCORE:
        passed += 1
    if score < lowest:
        lowest = score

average = total / number_of_students

print("Total score:", total)
print("Average score:", round(average, 2))
print("Passed:", passed)
print("Lowest score:", lowest)
