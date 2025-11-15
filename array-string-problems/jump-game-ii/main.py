class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = 0
        current_index = 0
        while current_index < len(nums) - 1:
            if current_index + nums[current_index] >= len(nums) -1:
                jumps += 1
                break
            largest_reach = 0
            best_index = current_index
            for k in range(
                current_index + 1,
                min(current_index + 1 + nums[current_index], len(nums)),
            ):
                if k + nums[k] >= largest_reach:
                    largest_reach = k + nums[k]
                    best_index = k
            current_index = best_index
            jumps += 1
        return jumps


if __name__ == "__main__":
    assert Solution().jump([2, 3, 1, 1, 4]) == 2
    assert Solution().jump([2, 3, 0, 1, 4]) == 2
    assert Solution().jump([3,2,1]) == 1
