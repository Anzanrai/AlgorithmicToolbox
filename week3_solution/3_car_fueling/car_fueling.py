# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    stops
    num_refills = 0
    current_refill = 0
    while current_refill <= len(stops)-2:
        last_refill = current_refill
        while current_refill <= len(stops)-2 and stops[current_refill+1]-stops[last_refill] <= tank:
            current_refill += 1
        if current_refill == last_refill:
            return -1
        if current_refill <= len(stops)-2:
            num_refills += 1

    return num_refills


if __name__ == '__main__':
    d = int(input())
    m = int(input())
    n = int(input())
    stops = list(map(int, input().split()))
    stops.append(0)
    stops.append(d)
    print(compute_min_refills(d, m, sorted(stops)))
