LAST_DIGIT = 4  # change to the last digit of your NIM
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []
total = 0
limit = 0

# untuk input
for i in range(7):
    daily = int(input(f"Day {i + 1}: "))
    expenses.append(daily)
    total += daily

    if daily > daily_limit:
        limit += 1

# perhitungan
average = total / len(expenses)
highest = max(expenses)
highest_day = expenses.index(highest) + 1

# output
print(f"Daily limit: {daily_limit}")
print(f"Total: {total}")
print(f"Average: {average:.1f}")
print(f"Highest: day {highest_day} ({highest})")
print(f"Days above limit: {limit}")