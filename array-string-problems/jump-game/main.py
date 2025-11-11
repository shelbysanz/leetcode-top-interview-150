class Solution:
    def canJump(self, nums: list[int]) -> bool:
        jump_value = 0
        for i in range(len(nums) - 1,  -1, -1):
            if nums[i] >= jump_value:
                jump_value = 0
            jump_value += 1
        return jump_value == 1

if __name__ == "__main__":
    assert Solution().canJump([2,3,1,1,4]) == True
    assert Solution().canJump([2,0]) == True
    assert Solution().canJump([0]) == True
