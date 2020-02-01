# Uses python3
import sys


def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


def gcd_euclid(a, b):
    if b == 0:
        return a
    elif a > b:
        if a % b != 0:
            return gcd_euclid(b, a%b)
        else:
            return b
    else:
        if b % a != 0:
            return gcd_euclid(a, b%a)
        else:
            return a


def lcm_fast(a, b):
    gcd = gcd_euclid(a, b)
    factor_a = a // gcd
    factor_b = b // gcd
    return gcd * factor_a * factor_b


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm_fast(a, b))

