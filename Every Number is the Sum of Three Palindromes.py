from itertools import product

def gen_palindrome_numbers(max):
    for x in range(max+1):
        x = str(x)
        if x == x[::-1]:
            yield int(x)

def find_sum_equation(num):
    palindrome_numbers = [x for x in gen_palindrome_numbers(num)]
    checked = []
    for x in product(palindrome_numbers, repeat=3):
        if sum(x) == num:
            x = sorted(x)
            if x not in checked:
                yield x
                checked.append(x)

for x in find_sum_equation(3141592):
    print(' + '.join([str(y) for y in x]) + ' = 3141592')