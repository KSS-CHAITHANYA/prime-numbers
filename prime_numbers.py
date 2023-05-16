import math

given_number = 36


A = [2]

for n in range(2, given_number):
    count = 0
    for j in range(2, math.ceil(n**0.5) + 1):
        if n % j == 0:
            count += 1
    if count == 0:
        A.append(n)

print(A)
