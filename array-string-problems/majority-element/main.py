class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counter = 0
        value = 0
        for i in nums:
            if counter == 0:
                value = i
            if value == i:
                counter += 1
            else:
                counter -= 1
        return value
