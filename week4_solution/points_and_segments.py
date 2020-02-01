# Uses python3
from collections import namedtuple

Coordinate = namedtuple('Coordinate', ['coordinate', 'type', 'index'])


def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    point_tuples = []
    for i in range(len(starts)):
        point_tuples.append(Coordinate(starts[i], 'l', i))
        point_tuples.append(Coordinate(ends[i], 'r', i))
    point_tuples = point_tuples + [Coordinate(points[i], 'p', i) for i in range(len(points))]
    point_tuples = sorted(point_tuples)
    coverage = 0
    for point_tuple in point_tuples:
        if point_tuple.type == 'l':
            coverage += 1
        elif point_tuple.type == 'r':
            coverage -= 1
        elif point_tuple.type == 'p':
            cnt[point_tuple.index] = coverage
        else:
            assert False
    #write your code here
    return cnt


def naive_count_segments(starts, ends, points):
    cnt = []
    for i in points:
        count = 0
        for j in range(len(starts)):
            if starts[j] <= i <= ends[j]:
                count += 1
        cnt.append(count)
    return cnt


if __name__ == '__main__':
    num_segments, num_points = list(map(int, input().split()))
    starts = []
    ends = []
    for i in range(num_segments):
        start, end = list(map(int, input().split()))
        starts.append(start)
        ends.append(end)
    points = list(map(int, input().split()))
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
