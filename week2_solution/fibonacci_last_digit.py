# Uses python3
import sys


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10

    return current % 10

    # using binet's formula to calculate nth term of fibonacci sequence.
    # fn = ((1.618033988749895**n) -(1-1.618033988749895)**n) / float (5**0.5)
    # fn = 1/(5**(1/2)) * (((1+5**(1/2))/2)**n - ((1-5**(1/2))/2)**n)
    # return int(fn % 10)


if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit_naive(n))
