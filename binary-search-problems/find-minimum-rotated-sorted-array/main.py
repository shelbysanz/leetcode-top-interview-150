class Solution:
    def findMin(self, nums: list[int]) -> int:
        if not nums:
            # leetcode constraints state this should never happen
            # so i'm adding an exception here if it does
            raise Exception("This shouldn't happen!")
        left, right = 0, len(nums) - 1
        if nums[left] <= nums[right]:
            return nums[0]
        while left <= right:
            mid = left + (right - left) // 2
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        # the execution should never reach down here, so throwing
        # an exception if it does
        raise Exception("This shouldn't happen!")
