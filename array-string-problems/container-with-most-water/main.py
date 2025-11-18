class Solution:
    def maxArea(self, height: list[int]) -> int:
        start = 0
        stop = len(height) - 1
        best_area = 0
        while start < stop:
            shortest_height = min(height[start], height[stop])
            distance_between = stop - start
            best_area = max(shortest_height * distance_between, best_area)
            if height[start] > height[stop]:
                stop -= 1
            else:
                start += 1
        return best_area

if __name__ == "__main__":
    assert Solution().maxArea([1,8,6,2,5,4,8,3,7]) == 49
