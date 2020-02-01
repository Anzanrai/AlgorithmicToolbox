# Uses python3
import sys


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
        sum = sum + current % 10
        sum_sequence.append(sum % 10)
    return period, sum_sequence, sum


def fibonacci_sum_naive(n):
    # this problem can be solved using the rule of periodicity that have been implemented previously
    # in this case, the periodicity is calculated for the sum rather than current value
    if n <= 1:
        return n

    # previous = 0
    # current = 1
    # sum = 1
    # sequence = [previous, current]
    # sum_sequence = [0, 1]
    # period = 0
    #
    # for _ in range(n - 1):
    #     previous, current = current, previous + current
    #     # sequence.append(current)
    #     if _ > 2 and (sum % 10 == 0 and (sum + current) % 10 == 1):
    #         period = _ + 1
    #         sum_sequence.pop(-1)
    #         break
    #     sum += current
    #     sum_sequence.append(sum % 10)
    # print(sum_sequence)
    # return sum % 10

    period, sum_sequence, sum = get_period_and_sum_sequence()

    if period == 0:
        return sum % 10
    else:
        remainder = n % period
        return sum_sequence[remainder]
    # print(sequence)


if __name__ == '__main__':
    # input = sys.stdin.read()
    n = int(input())
    print(fibonacci_sum_naive(n))
    # fibonacci_sum_naive(n)