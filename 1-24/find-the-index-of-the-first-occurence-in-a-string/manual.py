"""If I couldn't use the built-in python method I would use the sliding window method"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_length = len(needle)
        i = 0
        while i + needle_length <= len(haystack):
            if haystack[i : i + needle_length] == needle:
                return i
            i += 1
        return -1
