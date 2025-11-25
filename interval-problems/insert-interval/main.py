def search_start(arr: list[list[int]], value: int):
    """looking for the first index where arr[i][1] >= value"""
    low = 0
    high = len(arr)
    while low < high:
        mid = low + (high - low) // 2
        if arr[mid][1] < value:
            low = mid + 1
        else:
            high = mid
    return low


def search_end(arr: list[list[int]], value: int):
    """looking for the first index where arr[0] > value"""
    low = 0
    high = len(arr)
    while low < high:
        mid = low + (high - low) // 2
        if arr[mid][0] <= value:
            low = mid + 1
        else:
            high = mid
    return low


class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:

        starting = search_start(intervals, newInterval[0])
        ending = search_end(intervals, newInterval[1])

        result: list[list[int]] = intervals[
            :starting
        ]  # add items before the starting index

        if starting == ending:  # handle no overlap, no merge needed
            result.append(newInterval)
        else:  # handler overlap, merge needed
            result.append(
                [
                    min(intervals[starting][0], newInterval[0]),
                    max(intervals[ending - 1][1], newInterval[1]),
                ]
            )

        result.extend(intervals[ending:])  # add remaining items after ending index

        return result
