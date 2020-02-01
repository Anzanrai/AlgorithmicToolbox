# Uses python3
import sys


def get_change(m):
    #write your code here
    coins = [1, 3, 4]
    min_num_coins = [0]
    for money in range(1, m+1):
        min_num_coins.append(sys.maxsize)
        for i in coins:
            if money >= i:
                num_coins = min_num_coins[money-i]+1
                if num_coins < min_num_coins[money]:
                    min_num_coins[money] = num_coins
    return min_num_coins[money]


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
