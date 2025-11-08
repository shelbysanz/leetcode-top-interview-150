class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap: dict[int, int] = {}
        for i in range(0, len(nums)):
            value = target - nums[i]
            index = hashmap.get(value)
            if index is not None:
                return [i, index]
            hashmap[nums[i]] = i
        return []
