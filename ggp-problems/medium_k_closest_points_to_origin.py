import random


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def getSqrtVal(point):
            return point[0] ** 2 + point[1] ** 2

        def quickselect(l, r):
            while True:
                if l >= r:
                    return points[:k]

                l_tmp, r_tmp = l, r
                pivot = getSqrtVal(points[random.randint(l_tmp, r_tmp)])

                while l_tmp <= r_tmp:
                    while getSqrtVal(points[l_tmp]) < pivot:
                        l_tmp += 1
                    while getSqrtVal(points[r_tmp]) > pivot:
                        r_tmp -= 1
                    if l_tmp <= r_tmp:
                        points[l_tmp], points[r_tmp] = points[r_tmp], points[l_tmp]
                        l_tmp += 1
                        r_tmp -= 1

                if k - 1 <= r_tmp:
                    r = r_tmp
                elif k - 1 >= l_tmp:
                    l = l_tmp
                else:
                    return points[:k]

        return quickselect(0, len(points) - 1)
