# Uses python3


def edit_distance(s, t):
    #write your code here
    distance_mat = [[0]*(len(t)+1) for i in range(len(s)+1)]

    for i in range(1, len(s)+1):
        distance_mat[i][0] = i

    for j in range(1, len(t)+1):
        distance_mat[0][j] = j

    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            insertion_cost = distance_mat[i][j-1] + 1
            deletion_cost = distance_mat[i-1][j] + 1
            match_cost = distance_mat[i-1][j-1]
            mismatch_cost = distance_mat[i-1][j-1] + 1

            if s[i-1] == t[j-1]:
                distance_mat[i][j] = min(insertion_cost, deletion_cost, match_cost)
            else:
                distance_mat[i][j] = min(insertion_cost, deletion_cost, mismatch_cost)

    return(distance_mat[i][j])


if __name__ == "__main__":
    first = input()
    second = input()
    print(edit_distance(first, second))
