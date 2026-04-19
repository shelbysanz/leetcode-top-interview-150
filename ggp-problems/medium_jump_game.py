class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumps_needed = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] >= jumps_needed:
                jumps_needed = 0
            jumps_needed += 1
        return jumps_needed == 1
