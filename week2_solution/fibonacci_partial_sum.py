# Uses python3
import sys


def fibonacci_partial_sum_naive(from_, to):
    total = 0
    previous = 0
    current = 1

    for i in range(to + 1):
        if i >= from_:
            total += previous

        previous, current = current, previous + current

    return total % 10


def get_periodicity():
    previous = 0
    current = 1
    period = 0
    sequence = [previous, current]

    while True:
        previous, current = current, (previous + current) % 10
        period += 1
        sequence.append(current%10)
        if previous % 10 == 0 and current % 10 == 1:
            sequence.pop(-1)
            sequence.pop(-1)
            break
    # print(period)
    # print(len(sequence))
    return period, sequence


def fibonacci_partial_sum_fast(from_, to):
    # period, sum_sequence, sum = get_period_and_sum_sequence()
    # difference = to - from_
    # if to < period:
    #     fibonacci_partial_sum_naive(from_, to)
    # else:
    period, sequence = get_periodicity()
    difference = to - from_
    remainder = from_ % period
    if difference > period:
        difference_remainder = difference % period
        # print(sequence[remainder:remainder+difference_remainder+1])
        if remainder+difference_remainder+1 > period:
            end_point = ((remainder+difference_remainder+1) % period) + 1
        else:
            end_point = difference_remainder+ 1
        total = sum(sequence[remainder:remainder+end_point])
    else:
        # print(sequence[remainder:difference+remainder+1])
        total = sum(sequence[remainder:difference+remainder+1])
    return total % 10


if __name__ == '__main__':
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum_fast(from_, to))