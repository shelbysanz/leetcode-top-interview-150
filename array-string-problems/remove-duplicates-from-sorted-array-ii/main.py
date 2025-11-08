class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        current_index = 2
        for i in range(2, len(nums)):
            if not (
                nums[current_index - 1] == nums[i]
                and nums[current_index - 2] == nums[i]
            ):
                nums[current_index] = nums[i]
                current_index += 1
        return current_index
