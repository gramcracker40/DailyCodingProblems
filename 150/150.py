'''
Good morning! Here's your coding interview problem for today.

This problem was asked by LinkedIn.

Given a list of points, a central point, and an integer k, 
find the nearest k points from the central point.

For example, given the list of points [(0, 0), (5, 4), (3, 1)], 
the central point (1, 2), and k = 2, return [(0, 0), (3, 1)].
'''
import math


data = [(0, 0), (5, 4), (3, 1), (8,11), (12,13), (1,3)]
c_point = (1, 2)
k = 3


def distance(x1, y1, x2, y2):
    return round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 3)


dists = [(100000,(123,123))]
for count, each in enumerate(data):
    dist = distance(c_point[0], c_point[1], each[0], each[1])
    highest = dists.index(max(dists, key=lambda k: k[0])) if dists else 0
    if dist < dists[highest][0] and len(dists) < k:
        dists.append((dist,each))
    elif dist < dists[highest][0] and len(dists) == k:
        dists[highest] = (dist, each)


for all in dists:
    print(all[1], end=" ")