class Solution:
    def reverseWords(self, s: str) -> str:
        s_array = reversed(s.split())
        return " ".join(s_array)
