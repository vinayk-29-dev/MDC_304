# Question 1: Numbers divisible by 7 but not by 3
# Find numbers between 2000 and 3200 (inclusive).

numbers = []

for number in range(2000, 3201):
    if number % 7 == 0 and number % 3 != 0:
        numbers.append(str(number))

print(",".join(numbers))
