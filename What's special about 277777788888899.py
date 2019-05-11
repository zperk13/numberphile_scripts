# https://youtu.be/Wim9WJeDTHQ
from random import randint


def multiplication_persistence(x, print_steps=False):
    def multiply_digits(y):
        result = 1
        for digit in str(y):
            digit = int(digit)
            result *= digit
        return result

    steps = 0
    if print_steps:
        print(x)
        while len(str(x)) > 1:
            x = multiply_digits(x)
            print(f'{x:,}')
            steps += 1
        return steps
    else:
        while len(str(x)) > 1:
            x = multiply_digits(x)
            steps += 1
        return steps


def find_multiplication_persistence(max_num, print_if_equal=False, start_num=1):
    num = start_num
    best = 1
    # I know the repeating of code is ugly,
    # I'm just speeding it up by making it not do an unnecessary if statement every number
    if print_if_equal:
        while num < max_num:
            result = multiplication_persistence(num)
            if result >= best:
                print(f'Number found: {num:,} with {result} steps')
                best = result
            num += 1
    else:
        while num < max_num:
            result = multiplication_persistence(num)
            if result > best:
                print(f'Number found: {num:,} with {result} steps')
                best = result
            num += 1


def random_find_multiplication_persistence(min_num, max_num):
    num = min_num
    best = 1
    while num < max_num:
        result = multiplication_persistence(num)
        if result > best:
            print(f'Number found: {num:,} with {result} steps')
            best = result
        num = randint(min_num, max_num)


def smart_random_find_multiplication_persistence():
    best = 1
    while True:
        num_list = ['2', '6', '7', '8', '9']
        string = ''
        for _ in range(randint(232, 250)):
            index = randint(0, len(num_list) - 1)
            string += num_list[index]
            num_list = num_list[index:]
        number = int(string)
        result = multiplication_persistence(number)
        if result > best:
            print(f'Number found: {number:,} with {result} steps')
            best = result


if __name__ == '__main__':
    title_number = 277_777_788_888_899
    # print(multiplication_persistence(title_number))
    # find_multiplication_persistence(title_number+1)
    # find_multiplication_persistence(int('1'+'0'*250), start_num=int('1'+'0'*232))
    # randint(int('1' + '0' * 232), int('1' + '0' * 250))
    # random_find_multiplication_persistence(int('1' + '0' * 232), int('1' + '0' * 250))
    smart_random_find_multiplication_persistence()
