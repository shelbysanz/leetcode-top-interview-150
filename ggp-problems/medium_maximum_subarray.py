class Solution:
    def maxSubArray(self, nums: list[int]) -> int | None:
        if not nums:
            return
        n = len(nums)
        max_sum = nums[0]
        prev = nums[0]
        for i in range(1,n):
            prev = max(prev + nums[i], nums[i])
            max_sum = max(max_sum, prev)
        return max_sum
