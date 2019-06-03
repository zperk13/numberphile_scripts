# https://youtu.be/Jwtn5_d2YCs
import time

from math import pi


def tortoise():
    print('1 + 1/2 + 1/4 + 1/8 ... = 2')
    num = 1
    denominator = 2
    while num != 2:
        print(num)
        num += 1 / denominator
        denominator *= 2
    print(num)


def infinity_2(stopping_point, print_num=False, track_time=False):
    if track_time:
        start_time = time.time()
    # Even though I'm copying my code and it doesn't look good,
    # it's faster because I'm not checking if print_num is True every single step
    num = 1
    denominator = 2
    if print_num:
        while num < stopping_point:
            print(num)
            num += 1 / denominator
            denominator += 1
    else:
        while num < stopping_point:
            num += 1 / denominator
            denominator += 1
    end_time = time.time()
    steps = denominator - 2
    print(f'{num} reached in {steps:,} steps. The denominator was {denominator - 1:,}', end="")
    if track_time:
        print(f' and took {end_time - start_time} to complete')


def infinity_3(max_num):
    print('1 + (1/2)^2 + (1/3)^2 ...')
    num = 1
    denominator = 2
    while denominator < max_num:
        num += (1 / denominator) ** 2
        denominator += 1
    print(num)


if __name__ == '__main__':
    tortoise()
    print('\n\n\n...starting calculation for infinite series 2, wait for it to calculate...')
    infinity_2(20, track_time=True)
    print('\n\ninfinity series 3 now\n')
    infinity_3(1_000_000)
    print('eventually it would reach pi^2/6 which is about', ((pi ** 2) / 6))
