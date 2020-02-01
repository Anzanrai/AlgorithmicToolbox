# Uses python3
def calc_fib(n):
    if n <= 1:
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


def calc_fib_fast(n):
    a = 0
    b = 1
    fib_seq = [a, b]
    if -1 < n <= 1:
        return fib_seq[n]
    else:
        for i in range(2, n+1):
            fib_seq.append(fib_seq[i-2]+fib_seq[i-1])
    return fib_seq.pop(-1)


n = int(input())

print(calc_fib_fast(n))
