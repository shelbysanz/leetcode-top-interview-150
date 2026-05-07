from sortedcontainers import SortedList


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen, output = SortedList([]), [0] * n
        for i in range(n - 1, -1, -1):
            idx = seen.bisect_left(nums[i])
            output[i] = idx
            seen.add(nums[i])
        return output
