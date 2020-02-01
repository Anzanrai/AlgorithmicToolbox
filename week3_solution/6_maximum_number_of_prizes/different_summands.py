# Uses python3
import math


def optimal_summands(n):
    total_sum = n
    optional_summands = list(range(1, n))
    summands = []
    while n and len(optional_summands):
        first_summand = optional_summands.pop(-1)
        for x in optional_summands[0:int(math.ceil(math.sqrt((total_sum+1)/2)))]:
            if first_summand + x > n:
                break
            if first_summand + x == n and x not in summands:
                summands.append(optional_summands.pop(optional_summands.index(x)))
                n = first_summand
                break
    if sum(summands) != total_sum:
        summands.append(n)
    return summands


def optimal_summands_less_memory(n):
    k = math.floor((math.sqrt(8*n+1)-1)/2)
    summands = list(range(1, k))
    summands.append(n-sum(summands))
    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands_less_memory(n)
    print(len(summands))
    sol = " ".join(map(str, summands))
    print(sol)
