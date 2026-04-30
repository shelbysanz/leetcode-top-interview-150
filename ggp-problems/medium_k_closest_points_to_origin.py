import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        counter = 0
        for x, y in points:
            sqrt_val = x ** 2 + y ** 2
            counter += 1
            heapq.heappush(heap, (-sqrt_val, counter, [x, y]))
            if len(heap) > k:
                heapq.heappop(heap)

        return [i[2] for i in heap]
