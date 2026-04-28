class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        prev_seat_i = None
        max_dist = float('-inf')
        curr_dist = 0
        for i in range(len(seats)):
            if seats[i] == 0:
                curr_dist += 1
                continue
            if prev_seat_i is not None:
                curr_dist = (i - prev_seat_i) // 2
            max_dist = max(max_dist, curr_dist)
            curr_dist = 0  
            prev_seat_i = i
        max_dist = max(max_dist, curr_dist)
        return max_dist
