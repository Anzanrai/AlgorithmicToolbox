#Uses python3
from collections import namedtuple

coordinate_point = namedtuple('coordinate_point', ['x', 'y'])


def calculated_min_distance(points):
    calculated_distances = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            calculated_distances.append(calculate_distance(points[i], points[j]))
    return min(calculated_distances)


def calculate_distance(p1, p2):
    return ((p1.x - p2.x)**2+(p1.y - p2.y)**2)**(1/2)


def calculate_minimum_strip_distance(strip_points, min_distance):
    min_dist = min_distance
    for i in range(len(strip_points)):
        for j in range(i+1, len(strip_points)):
            distance = calculate_distance(strip_points[i], strip_points[j])
            if distance < min_dist:
                min_dist = distance
    return min_dist


def calculate_minimum_distance(points):
    #write your code here
    if len(points) <= 3:
        return calculated_min_distance(points)
    mid_value = len(points)//2
    section_l = calculate_minimum_distance(points[:mid_value])
    section_r = calculate_minimum_distance(points[mid_value::])
    minimum_distance = min(section_l, section_r)

    mid_point = points[mid_value]
    strip_points = [point for point in points if abs(mid_point.x - point.x) < minimum_distance]

    if len(strip_points) > 1:
        minimum_distance = calculate_minimum_strip_distance(strip_points, minimum_distance)
    return minimum_distance


if __name__ == '__main__':
    num_points = int(input())
    points = []
    for i in range(num_points):
        x, y = list(map(int, input().split()))
        points.append(coordinate_point(x, y))
    points = sorted(points)
    min_distance = calculate_minimum_distance(points)
    print(min_distance)
