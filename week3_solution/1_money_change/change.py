# Uses python3


def get_change(m):
    #write your code here
    denominations = [1, 5, 10]
    remainder = m
    change = 0
    for denomination in denominations[::-1]:
        if remainder >= denomination:
            change += remainder // denomination
            remainder = remainder % denomination
    return change


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
