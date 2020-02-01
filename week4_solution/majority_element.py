# Uses python3


def get_majority_element(a):
    item_dict = {}
    for item in a:
        if item in item_dict.keys():
            count = item_dict.get(item)
            item_dict.update({item: count+1})
        else:
            item_dict.update({item: 1})
    majority_count = max(item_dict.values())
    if majority_count > n//2:
        return 1
    else:
        return 0


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)
    print(get_majority_element(a))
