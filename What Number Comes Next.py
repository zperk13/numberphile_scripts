# https://youtu.be/OeGSQggDkxI


def print_holes(number_of_prints):
    for x in range(number_of_prints):
        if x == 0:
            print(1)
        else:
            if x % 2 == 0:
                print(int('8' * int(x / 2)))
            else:
                print(int('4' + '8' * int((x - 1) / 2)))


def six(max):
    string = ''
    for x in range(1, max + 1):
        string += str(6 * x)
    print(string)
    for y in range(2, len(string) + 1, 2):
        print(string[y - 2:y])


def roman(name_of_number):
    for letter in name_of_number.upper():
        if letter in ['I', 'V', 'X', 'L', 'C', 'D', 'M']:
            print(letter, end='')


def gen_emirps(max):
    def is_even(integer):
        # Returns True if integer given is even, else it will return False
        return integer % 2 == 0

    def is_prime(number):
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

    for x in range(3, max + 1, 2):
        if is_prime(x):
            reverse = int(str(x)[::-1])
            if is_prime(reverse):
                print(x, reverse)
