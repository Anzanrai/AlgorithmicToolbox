#Uses python3

import sys


def lcs2(s, t):
    #write your code here
    distance_mat = [[0] * (len(t) + 1) for i in range(len(s) + 1)]

    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i - 1] == t[j - 1]:
                distance_mat[i][j] = distance_mat[i-1][j-1]+1
            else:
                distance_mat[i][j] = max(distance_mat[i-1][j], distance_mat[i][j-1])
    # sub_sequence_len = backtrack_sequence(distance_mat, i, j, s, t)
    return distance_mat[i][j]


def backtrack_sequence(distance_mat, i, j, s, t):
    sub_sequence_len = 0
    while i > 0 or j > 0:
        if i > 0 and distance_mat[i][j] == distance_mat[i-1][j]-1:
            i -= 1
        elif j > 0 and distance_mat[i][j] == distance_mat[i][j-1]-1:
            j -= 1
        else:
            if s[i-1] == t[j-1]:
                sub_sequence_len += 1
            i -= 1
            j -= 1

    return sub_sequence_len


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    print(lcs2(a, b))
