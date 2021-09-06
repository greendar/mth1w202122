# Program to determine the number of 7 digits in all the numbers from 1 - 1000

strOut = ""

for i in range(1, 1001):
    strOut += str(i)

n = 0

for digit in strOut:
    if digit == '7':
        n += 1

print(n)
