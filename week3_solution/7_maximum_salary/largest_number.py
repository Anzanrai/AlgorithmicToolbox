#Uses python3

import sys


def largest_number(a):
    # write your code here
    temp = list(set(a.copy()))
    res = ""
    while len(a):
        max_digit = get_safe_max_digit(a)
        res += max_digit
        a.pop(a.index(max_digit))
    return res
    # max_digit = 0
    # while len(a) > 1:
    #     max_digit = max(a)
    #     if max_digit >= 10:
    #         temp.pop(temp.index(max_digit))
    #         if len(temp) and str(max_digit)+str(max(temp)) < str(max(temp))+str(max_digit):
    #             max_temp = max_digit
    #             max_digit = max(temp)
    #             temp.append(max_temp)
    #         else:
    #             temp.append(max_digit)
    #     res += str(max_digit)
    #     a.pop(a.index(max_digit))
    #     if max_digit not in a:
    #         temp.pop(temp.index(max_digit))
    # res += str(max(a))
    # return res


# def largest_number(data):

def get_safe_max(a, b):
    if a+b > b+a:
        return a
    return b


def get_safe_max_digit(a):
    max_digit = a[0]
    if len(a) > 1:
        for i in range(1, len(a)):
            max_digit = get_safe_max(max_digit, a[i])
        return max_digit
    else:
        return a[0]


if __name__ == '__main__':
    n = int(input())
    data = input().split()
    print(largest_number(data))

