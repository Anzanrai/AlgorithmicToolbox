# Uses python3


def merge(first_part, second_part):
    sorted_arr = []
    i = j = 0
    inversions = 0
    while i < len(first_part) and j < len(second_part):
        if first_part[i] <= second_part[j]:
            sorted_arr.append(first_part[i])
            i += 1
        else:
            sorted_arr.append(second_part[j])
            j += 1
            inversions += (len(first_part) - i)
    sorted_arr += first_part[i:]
    sorted_arr += second_part[j:]
    return sorted_arr, inversions


def merge_sort(a):
    if len(a) == 1:
        return a, 0
    mid = len(a)//2
    first_part, first_inversion = merge_sort(a[:mid])
    second_part, second_inversion = merge_sort(a[mid::])
    sorted_array, merge_inversion = merge(first_part, second_part)
    total_inversions = first_inversion+second_inversion+merge_inversion
    return sorted_array, total_inversions


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    sorted_array, num_of_inversions = merge_sort(a)
    print(num_of_inversions)
