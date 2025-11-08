class Solution:
    def isPalindrome(self, s: str) -> bool:
        # sanitize string
        s_array: list[str] = []
        for i in s:
            if i.isalnum():
                s_array.append(i.lower())

        # determine palindrome
        start = 0
        stop = len(s_array) - 1
        while start < stop:
            if s_array[start] != s_array[stop]:
                return False
            start += 1
            stop -= 1
        return True
