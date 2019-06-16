# https://youtu.be/ZMkIiFs35HQ


def generate_primes(max):
    def is_even(integer):
        # Returns True if integer given is even, else it will return False
        return integer % 2 == 0

    def is_prime(number, progress_bar=False):
        # Returns True if number given is prime, else it will return False
        # Making progress_bar=True will make a progress bar to see how far along it is at calculating the factors using tqdm
        if not isinstance(number, int):
            raise TypeError('number must be an integer')
        elif number < 1:
            raise ValueError('number must be at least 2')
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

    # Generates primes from 1 to max (inclusive)
    for x in range(5, max + 1, 2):
        if is_prime(x):
            yield x


for prime in generate_primes(65532):
    squared = prime ** 2
    one_less = squared - 1
    print(f'''{prime}^2={squared}
{prime}-1={one_less}
{one_less}/24={one_less / 24}''')
    print('\n\n')
