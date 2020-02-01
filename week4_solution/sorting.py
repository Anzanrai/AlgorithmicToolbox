# Uses python3
import random


def partition3(a, l, r):
    x = a[l]
    m_one = i = l
    m_two = r
    while i <= m_two:
        if a[i] < x:
            a[i], a[m_one] = a[m_one], a[i]
            m_one += 1
        if a[i] > x:
            a[i], a[m_two] = a[m_two], a[i]
            m_two -= 1
            i -= 1
        i += 1
    return m_one, m_two


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m_one, m_two = partition3(a, l, r)
    randomized_quick_sort(a, l, m_one - 1);
    randomized_quick_sort(a, m_two + 1, r);


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().strip().split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
