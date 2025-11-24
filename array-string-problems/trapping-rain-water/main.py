class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
        total_count = 0
        start = 0
        end = len(height) - 1
        start_max = height[start]
        end_max = height[end]
        while start < end:
            if height[start] <= height[end]:
                start += 1
                start_max = max(start_max, height[start])
                total_count += start_max - height[start]
            else:
                end -= 1
                end_max = max(end_max, height[end])
                total_count += end_max - height[end]
        return total_count


if __name__ == "__main__":
    assert Solution().trap([4,2,0,3,2,5]) == 9
    assert Solution().trap([4, 2, 3]) == 1
