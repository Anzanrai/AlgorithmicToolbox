# Uses python3
import sys


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1
    period = 0

    # first calculate the period for repetition of the modulo
    for _ in range(n-1):
        previous, current = current, (previous + current) % m
        if _ > 2 and previous == 0 and current == 1:
            period = _ + 1
            break

    if period == 0:
        return current % m
    else:
        remainder = n % period
        previous = 0
        current = 1

        for _ in range(remainder-1):
            previous, current = current, (previous + current) % m
        return current % m


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(get_fibonacci_huge_naive(n, m))
