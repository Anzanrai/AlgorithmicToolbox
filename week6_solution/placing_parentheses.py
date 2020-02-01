# Uses python3
import re
import sys


def evaluate_expression(a, b, op):
    if op == '+':
        return int(a) + int(b)
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def min_and_max(i, j, m, M, ops):
    min_val = sys.maxsize
    max_val = -sys.maxsize
    if len(range(j)):
        for k in range(i, j):
            a = evaluate_expression(M[i][k], M[k+1][j], ops[k])
            b = evaluate_expression(M[i][k], m[k+1][j], ops[k])
            c = evaluate_expression(m[i][k], M[k+1][j], ops[k])
            d = evaluate_expression(m[i][k], m[k+1][j], ops[k])
            if k == 0:
                min_val = min(a, b, c, d)
                max_val = max(a, b, c, d)
            else:
                min_val = min(min_val, a, b, c, d)
                max_val = max(max_val, a, b, c, d)
        return min_val, max_val
    else:
        return


def get_maximum_value(dataset):
    #write your code here
    digits = list(map(int, dataset[::2]))

    operations = dataset[1::2]
    m = [[0] * len(digits) for i in range(len(digits))]
    M = [[0] * len(digits) for i in range(len(digits))]
    for i in range(len(digits)):
        m[i][i] = digits[i]
        M[i][i] = digits[i]

    for s in range(1, len(digits)):
        for i in range(len(digits)-s):
            j = i+s
            if min_and_max(i, j, m, M, operations):
                m[i][j], M[i][j] = min_and_max(i, j, m, M, operations)

    return M[0][len(digits)-1]


if __name__ == "__main__":
    expression = re.split('(\W+)', input())
    print(get_maximum_value(expression))
