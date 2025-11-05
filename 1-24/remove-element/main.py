class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        current_index = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[current_index] = nums[i]
                current_index += 1
        return current_index
