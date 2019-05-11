# https://youtu.be/q6L06pyt9CA
# I wanted to do the program he did (and potentially beat him) but I don't know the formulas
from math import sqrt


def cannon(n):
    return int((n * (n + 1) * (2 * n + 1)) / 6)


cannon_numbers = []
number = 2
while True:
    cannon_num = cannon(number)
    number += 1
    cannon_numbers.append(cannon_num)
    if cannon_num > 5000:
        break
for x in cannon_numbers:
    root = sqrt(x)
    if int(root) == root:
        print(x)
