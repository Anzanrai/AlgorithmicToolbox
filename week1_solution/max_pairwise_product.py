# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    max_1 = -1
    max_2 = -1
    max_index_1 = -1
    max_index_2 = -1
    for first in range(n):
        if max_1 < numbers[first]:
            max_1 = numbers[first]
            max_index_1 = first

    for second in range(n):
        if max_2 < numbers[second] and max_index_1 != second:
            max_index_2 = second
            max_2 = numbers[second]
    max_product = numbers[max_index_1] * numbers[max_index_2]

    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
