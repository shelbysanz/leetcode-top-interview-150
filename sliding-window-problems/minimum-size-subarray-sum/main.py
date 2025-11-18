class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        start = 0
        window_sum = 0
        min_length = float("inf")

        for end in range(len(nums)):
            window_sum += nums[end]

            while window_sum >= target:
                min_length = min(end - start + 1, min_length)
                window_sum -= nums[start]
                start += 1

        return 0 if min_length == float("inf") else int(min_length)


if __name__ == "__main__":
    assert Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
    assert Solution().minSubArrayLen(11, [1, 2, 3, 4, 5]) == 3
