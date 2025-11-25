class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str: str = str(x)
        start = 0
        end = len(x_str) - 1
        while start < end:
            if x_str[start] != x_str[end]:
                return False
            start += 1
            end -= 1
        return True
