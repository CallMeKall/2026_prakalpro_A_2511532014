PASS_SCORE = 65

number_of_students = int(input("Number of students: "))

total = 0

for i in range(1, number_of_students + 1):
    print("Student", i)

    score = int(input("Enter score: "))

    while score < 0 or score > 100:
        print("Invalid score!")
        score = int(input("Enter score: "))
    total += score
average = total / number_of_students

print("Total score:", total)
print("Average score:", round(average, 2))