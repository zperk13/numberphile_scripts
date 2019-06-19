# https://youtu.be/cZkGeR9CWbk


def add(*args):
    args = [abs(int(x)) for x in args]
    max_len = max([len(str(x)) for x in args])
    padded_nums = []
    for num in args:
        new_num = '0'*(max_len-len(str(num)))+str(num)
        padded_nums.append(new_num)
    result = ''
    for digit in range(max_len):
        result += max([x[digit] for x in padded_nums if x[digit] != '0'])
    return result


if __name__ == '__main__':
    print(add(58, 19))