#Uses python3


def lcs3(a, b, c):
    # if any of the sequence is empty then there is no common subsequence hence return 0 in that case.
    if len(a) and len(b) and len(c):
        distance_mat = [[[0] * (len(c) + 1) for j in range(len(b) + 1)] for i in range(len(a) + 1)]
        # this program is designed with the optimal alignment algorithm such that value of mu, and sigma i.e.
        # mismatch and indel is assigned 0 and only the case of match is scored with 1

        # maximize the score such that the count is maintained for only the case of match in the provided sequences.
        for i in range(1, len(a) + 1):
            for j in range(1, len(b) + 1):
                for k in range(1, len(c) + 1):
                    if a[i-1] == b[j-1] and a[i-1] == c[k -1]:
                        distance_mat[i][j][k] = distance_mat[i - 1][j - 1][k - 1] + 1
                    else:
                        distance_mat[i][j][k] = max(distance_mat[i - 1][j][k], distance_mat[i][j - 1][k],
                                                    distance_mat[i][j][k-1])
        return distance_mat[i][j][k]
    else:
        return 0


def backtrack_sequence(distance_mat, i, j, s, t):
    sub_sequence = []
    while i > 0 or j > 0:
        if i > 0 and distance_mat[i][j] == distance_mat[i-1][j]+1:
            i -= 1
        elif j > 0 and distance_mat[i][j] == distance_mat[i][j-1]+1:
            j -= 1
        else:
            if s[i-1] == t[j-1]:
                sub_sequence.append(s[i-1])
            i -= 1
            j -= 1
    return sub_sequence


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    l = int(input())
    c = list(map(int, input().split()))
    print(lcs3(a, b, c))
