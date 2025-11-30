class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def findLeftmost(arr: list[int], target: int):
            left, right = 0, len(arr) - 1
            left_found = -1
            while left <= right:
                mid = left + (right - left) // 2
                if arr[mid] == target:
                    left_found = mid
                    right = mid - 1
                elif arr[mid] > target:
                    right = mid - 1
                elif arr[mid] < target:
                    left = mid + 1
            return left_found

        def findRightmost(arr: list[int], target: int):
            left, right = 0, len(arr) - 1
            right_found = -1
            while left <= right:
                mid = left + (right - left) // 2
                if arr[mid] == target:
                    right_found = mid
                    left = mid + 1
                elif arr[mid] > target:
                    right = mid - 1
                elif arr[mid] < target:
                    left = mid + 1
            return right_found

        return [findLeftmost(nums, target), findRightmost(nums, target)]
