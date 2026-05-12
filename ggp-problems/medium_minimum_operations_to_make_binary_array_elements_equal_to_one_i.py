class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1

        flips = 0
        l, r = 0, 2
        # increase them at the same pace
        while r < len(nums):
            if nums[l] == 0:
                for i in range(l, r + 1):
                    nums[i] = 0 if nums[i] == 1 else 1
                flips += 1
            l += 1
            r += 1
        if nums[l - 1 : r] != [1, 1, 1]:
            return -1

        return flips
