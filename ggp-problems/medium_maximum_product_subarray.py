class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_min = nums[0]
        max_prod = nums[0]
        for i in range(1, len(nums)):
            val = nums[i]
            prod_1 = curr_max * val
            prod_2 = curr_min * val
            curr_max = max(prod_1, prod_2, val)
            curr_min = min(prod_1, prod_2, val)
            max_prod = max(max_prod, curr_max, curr_min)
        return max_prod
