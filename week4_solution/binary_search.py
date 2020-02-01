# Uses python3


def binary_search(a, x):
    left, right = 0, len(a)
    while left < right:
        mid = (right + left) // 2
        if x == a[mid]:
            return mid
        if x > a[mid]:
            left = mid+1
        else:
            right = mid
    return -1

    # write your code here


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    n, *data_sequence = list(map(int, input().split()))
    k, *search_sequence = list(map(int, input().split()))

    for x in search_sequence:
        # replace with the call to binary_search when implemented
        print(binary_search(data_sequence, x), end=' ')
