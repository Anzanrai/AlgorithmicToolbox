# Uses python3
import sys


def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def remainder(a, b):
    return a % b, b


def gcd_euclid(a, b):
    if a > b:
        if a % b != 0:
            return gcd_euclid(b, a%b)
        else:
            return b
    else:
        if b % a != 0:
            return gcd_euclid(a, b%a)
        else:
            return a


if __name__ == "__main__":
    input_val = input()
    a, b = map(int, input_val.split())
    print(gcd_euclid(a, b))
