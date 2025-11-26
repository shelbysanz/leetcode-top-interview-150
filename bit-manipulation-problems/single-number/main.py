class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        if not nums:
            raise ValueError("leetcode constraints say this shouldn't be possible")

        result = 0
        for i in nums:
            result ^= i
        return result
