class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        current_index = 1
        for i in range(1, len(nums)):
            if nums[current_index - 1] != nums[i]:
                nums[current_index] = nums[i]
                current_index += 1
        return current_index
