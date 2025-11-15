class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:

        hashmap: dict[int, int] = {}

        for index, item in enumerate(nums):
            if item in hashmap and index - hashmap[item] <= k:
                return True
            hashmap[item] = index

        return False
