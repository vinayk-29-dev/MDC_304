# Question 3: Create a dictionary of numbers and their squares

n = int(input("Enter a number: "))
squares = {}

for i in range(1, n + 1):
    squares[i] = i * i

print(squares)
