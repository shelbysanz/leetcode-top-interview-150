class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(nums: list[int], start: int, stop: int):
            while start < stop:
                nums[stop], nums[start] = nums[start], nums[stop]
                start += 1
                stop -= 1

        n = len(nums)
        k = k % n

        reverse(nums, 0, n - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)
