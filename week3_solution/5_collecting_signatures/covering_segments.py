# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    points = []
    #write your code here
    while len(segments):
        min_end = min([s.end for s in segments])
        points.append(min_end)
        segments = [segment for segment in segments if not segment.start <= min_end <= segment.end]
        # for s in segments:
        #     if s.start <= min_end <= s.end:
        #         segments.pop(s)
    return points


if __name__ == '__main__':
    n = int(input())
    segments = []
    for i in range(n):
        x, y = list(map(int, input().split()))
        segments.append(Segment(x, y))
    # segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    segments = sorted(segments, key= lambda x: x[0])
    points = optimal_points(segments)
    # print(n)
    print(len(points))
    print(*points)
