class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        best_approx = 1
        left, right = 0, x // 2 + 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_square = mid * mid
            if mid_square <= x:
                if mid_square == x:
                    return mid
                best_approx = mid
                left = mid + 1
            else:
                right = mid - 1
        return best_approx
