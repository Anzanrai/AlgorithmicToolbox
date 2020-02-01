# Uses python3


def optimal_weight(W, w):
    # write your code here
    value = [[0] * (len(w)+1) for i in range(W+1)]
    result = 0
    for i in range(1, len(w)+1):
        for j in range(1, W+1):
            value[j][i] = value[j][i-1]
            if w[i-1] <= j:
                val = value[j-w[i-1]][i-1]+w[i-1]
                if value[j][i] < val:
                    value[j][i] = val
    return value[W][i]


if __name__ == '__main__':
    W, n = list(map(int, input().split()))
    w = list(map(int, input().split()))
    print(optimal_weight(W, w))
