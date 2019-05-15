def difference(num1, num2):
    return max([num1, num2]) - min([num1, num2])


def get_ant_numbers(antenna1, antenna2, head, thorax, abdomen):
    return [difference(antenna1, head), difference(antenna2, head), difference(head, thorax), difference(thorax, abdomen)]


if __name__ == '__main__':
    numbers = [1, 3, 5, 7, 9]
    count = 0
    for a1 in numbers:
        for a2 in [num for num in numbers if num not in [a1]]:
            for h in [num for num in numbers if num not in [a1, a2]]:
                for t in [num for num in numbers if num not in [a1, a2, h]]:
                    ab = [num for num in numbers if num not in [a1, a2, h, t]][0]
                    ant_numbers = get_ant_numbers(a1, a2, h, t, ab)
                    checked = []
                    for num in ant_numbers:
                        if num in checked:
                            break
                        else:
                            checked.append(num)
                    if len(checked) == 4:
                        count += 1
                        print(a1, a2, h, t, ab, checked)
    print(count)
