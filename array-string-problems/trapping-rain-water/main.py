class Solution:
    def trap(self, height: list[int]) -> int:
        total_count = 0
        while True:
            counting: bool = False
            count = 0
            should_break = True
            for i in height:
                if i:
                    if count:
                        total_count += count
                        count = 0
                    counting = True
                    should_break = False
                elif i == 0:
                    if counting:
                        count += 1
            if should_break:
                break
            height = [i - 1 if i > 0 else 0 for i in height]
        return total_count


if __name__ == "__main__":
    # assert Solution().trap([4,2,0,3,2,5]) == 9
    assert Solution().trap([4, 2, 3]) == 1
