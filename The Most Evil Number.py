# https://youtu.be/zk_Q9y_LNzg

from math import ceil
from time import time

max_num = 100_000_000


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

def gen_prime_list(max):
    if max <= 2:
        return []
    sieve = [x for x in range(3, max+1, 2)]
    top = len(sieve)
    for si in sieve:
        if si:
            bottom = (si * si - 3) // 2
            if bottom >= top:
                break
            sieve[bottom::si] = [0] * -((bottom - top) // si)
    return [2] + [el for el in sieve if el]

start = time()
print('Generating Primes')
primes = gen_prime_list(max_num)
print('Generated', len(primes), 'primes in', time() - start, 'seconds\n')


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


def gen_prime_index():
    for index, prime in enumerate(primes):
        index += 1
        index_sum = sum_digits(index)
        prime_sum = sum_digits(prime)
        if index_sum == prime_sum:
            yield [prime, index, index_sum]


def is_prime_index(num):
    if num not in primes:
        return False
    if sum_digits(num) == sum_digits(primes.index(num) + 1):
        return True
    return False


def right_side(num):
    string = str(num)
    length = len(string)
    return int(string[ceil(length / 2):])


def is_republican_prime(num):
    return right_side(num) in primes


def gen_republican_prime():
    for x in range(11, max_num + 1):
        right = right_side(x)
        if right in primes:
            yield [x, right]


def is_naughty_prime(num):
    if num not in primes:
        return False
    zero_count = 0
    other_count = 0
    for digit in str(num):
        if digit == '0':
            zero_count += 1
        else:
            other_count += 1
    return zero_count > other_count


def gen_naughty_prime():
    for x in range(1, max_num + 1, 2):
        if is_naughty_prime(x):
            yield x


def is_beastly_prime(num):
    if '666' in str(num):
        return num in primes


def gen_beastly_primes():
    for x in range(1, max_num + 1, 2):
        if is_beastly_prime(x):
            yield x
