# https://youtu.be/Wim9WJeDTHQ
def multiplication_persistence(x, print_steps=False):
    def multiply_digits(x):
        result = 1
        for digit in str(x):
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


def find_multiplication_persistence(max, print_if_equal=False, start_num=1):
    num = start_num
    best = 1
    # I know the repeating of code is ugly,
    # I'm just speeding it up so it doesn't do an unnecessary if statement every number
    if print_if_equal:
        while num < max:
            result = multiplication_persistence(num)
            if result >= best:
                print(f'Number found: {num:,} with {result} steps')
                best = result
            num += 1
    else:
        while num < max:
            result = multiplication_persistence(num)
            if result > best:
                print(f'Number found: {num:,} with {result} steps')
                best = result
            num += 1


if __name__ == '__main__':
    title_number = 277_777_788_888_899
    # print(multiplication_persistence(title_number))
    find_multiplication_persistence(title_number+1)
    # find_multiplication_persistence(int('1'+'0'*250), start_num=int('1'+'0'*232))