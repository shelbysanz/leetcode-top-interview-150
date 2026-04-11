import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        max_rooms = 0

        # first sort by start time
        intervals.sort(key=lambda i: i[0])

        heap = []
        # process them in order of start time
        # for each push the end time into a min heap
        for i in intervals:
            while heap and heap[0] <= i[0]:
                # pop min heap until the root is <= start of current meeting
                heapq.heappop(heap)
            # keep track of max len of the min heap (the amount is the current meetings at one time)
            heapq.heappush(heap, i[1])
            max_rooms = max(max_rooms, len(heap))

        return max_rooms
