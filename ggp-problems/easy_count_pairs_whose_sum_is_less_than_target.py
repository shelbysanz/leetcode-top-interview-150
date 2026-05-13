class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        l, r, pairs = 0, len(nums) - 1, 0
        while l < r:
            pair_sum = nums[l] + nums[r]
            if pair_sum < target:
                pairs += r - l
                l += 1
            else:
                r -= 1
        return pairs
