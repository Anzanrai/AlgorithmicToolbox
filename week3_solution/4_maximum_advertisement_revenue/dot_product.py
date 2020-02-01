#Uses python3


def max_dot_product(a, b):
    #write your code here
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a = sorted(a, reverse=True)
    b = sorted(b, reverse=True)
    print(max_dot_product(a, b))

