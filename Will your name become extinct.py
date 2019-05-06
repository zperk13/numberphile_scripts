# https://youtu.be/z34XhE5oRwo


def G(x):
    return (1 / 6) + ((2 / 6) * x) + ((2 / 6) * (x ** 2)) + ((1 / 6) * (x ** 3))


def difference(num1, num2):
    return max([num1, num2]) - min([num1, num2])


def main(sensitivity):
    result = []
    for x in range(1, 201):
        x = x / 100
        g = G(x)
        if difference(x, g) < sensitivity:
            result.append((x, g))
    return result


if __name__ == '__main__':
    for t in main(0.0025):
        print(t)
