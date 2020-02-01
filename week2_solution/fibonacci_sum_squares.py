# Uses python3
from sys import stdin


def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10


def get_period_and_sum_sequence():
    previous = 0
    current = 1
    sum = 1
    sum_sequence = [previous, current]
    period = 0

    for _ in range(100):
        previous, current = current, previous + current
        if _ > 2 and (sum % 10 == 0 and (sum + current) % 10 == 1):
            period = _ + 1
            sum_sequence.pop(-1)
            break
        sum = sum + (current**2 % 10)
        sum_sequence.append(sum % 10)
    return period, sum_sequence, sum


def fibonacci_sum_squares_fast(n):
    period, sum_sequence, sum = get_period_and_sum_sequence()

    if period == 0:
        return sum % 10
    else:
        remainder = n % period
        return sum_sequence[remainder]


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares_fast(n))
