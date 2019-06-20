# https://youtu.be/zk_Q9y_LNzg

from math import ceil


def is_even(integer):
    # Returns True if integer given is even, else it will return False
    return integer % 2 == 0


def is_prime(number):
    # Returns True if number given is prime, else it will return False
    # Making progress_bar=True will make a progress bar to see how far along it is at calculating the factors using tqdm
    if not isinstance(number, int):
        raise TypeError('number must be an integer')
    elif number < 1:
        return False
    factors = []
    if is_even(number) and number > 2:
        return False
    elif number == 1:
        return False
    else:
        for x in range(1, int(number + 1 / 2 + 3)):
            if number % x == 0:
                factors.append(x)
            if len(factors) > 2:
                return False
        return True


max_num = 1_000_000

primes = [x for x in range(1, max_num + 1, 2) if is_prime(x)]

def gen_belphegors_numbers(min):
    for n in range(min, max_num + 1):
        zeroes = '0' * n
        yield [int('1' + zeroes + '666' + zeroes + '1'), n]



def gen_belphegors_primes(min):  # SLOW
    for num, n in gen_belphegors_numbers(min):
        if num in primes:
            yield [num, n]


def sum_digits(num):
    return sum([int(x) for x in str(num)])


def prime_index():
    for index, prime in enumerate(primes):
        index_sum = sum_digits(index)
        prime_sum = sum_digits(prime)
        if index_sum == prime_sum:
            yield [prime, index, index_sum]


def republican_prime():
    def right_side(num):
        string = str(num)
        length = len(string)
        return int(string[ceil(length / 2):])

    for x in range(11, max_num + 1):
        right = right_side(x)
        if right in primes:
            yield [x, right]


def naughty_prime():
    for x in range(1, max_num + 1, 2):
        if x in primes:
            zero_count = 0
            other_count = 0
            for digit in str(x):
                if digit == '0':
                    zero_count += 1
                else:
                    other_count += 1
            if zero_count > other_count:
                yield x


def beastly_primes():
    for x in range(1, max_num + 1, 2):
        if '666' in str(x):
            if x in primes:
                yield x
