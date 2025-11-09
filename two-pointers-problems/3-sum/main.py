class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        results: list[list[int]] = []
        for i, item in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -item
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[left] + nums[right]
                if sum == target:
                    results.append([item, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif sum < target:
                    left += 1
                elif sum > target:
                    right -= 1
        return results
