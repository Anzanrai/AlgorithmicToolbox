# Uses python3
# import sys


def optimal_sequence(n):
    sequence = []
    ''' a list to store minimum number of operations required to formulate the index of the list
        i.e. no. of operations required to formulate 1 from 0 is 1 => 0+1 (1 operation)
        another example: 2 = 0+1+1 = 0+1*2 (2 operations)
        another example: 5 = 0+1*2*2+1 (5 operations)
        another example: 6 = 0+1*2*3 (4 operations)
    '''
    minimum_operation_count = [0] * (n + 1)
    for i in range(1, n + 1):
        minimum_operation_count[i] = minimum_operation_count[i - 1] + 1
        if i % 2 == 0:
            minimum_operation_count[i] = min(minimum_operation_count[i // 2] + 1, minimum_operation_count[i])
        if i % 3 == 0:
            minimum_operation_count[i] = min(minimum_operation_count[i // 3] + 1, minimum_operation_count[i])

    while n >= 1:
        sequence.append(n)
        if minimum_operation_count[n] == minimum_operation_count[n - 1] + 1:
            n = n - 1
        elif n % 2 == 0 and minimum_operation_count[n // 2] == minimum_operation_count[n] - 1:
            n = n // 2
        elif n % 3 == 0 and minimum_operation_count[n // 3] == minimum_operation_count[n] - 1:
            n = n // 3

    return reversed(sequence)

    # sequence = []
    # while n >= 1:
    #     sequence.append(n)
    #     if n % 3 == 0:
    #         n = n // 3
    #     elif n % 2 == 0:
    #         if (n-1) % 3 == 0:
    #             n = n - 1
    #         else:
    #             n = n // 2
    #     else:
    #         n = n - 1
    # return reversed(sequence)


n = int(input())
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
