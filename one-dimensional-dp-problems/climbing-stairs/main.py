class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return 0

        computed: dict[int, int] = {1: 1, 2: 2}

        def combinations(c: int) -> int:
            val = computed.get(c)
            if val is not None:
                return val

            val = combinations(c - 1) + combinations(c - 2)
            computed[c] = val
            return val

        return combinations(n)


if __name__ == "__main__":
    assert Solution().climbStairs(1) == 1
    assert Solution().climbStairs(2) == 2
    assert Solution().climbStairs(3) == 3
    assert Solution().climbStairs(4) == 5
    assert Solution().climbStairs(5) == 8
    assert Solution().climbStairs(10) == 89
    assert Solution().climbStairs(45) == 1836311903

