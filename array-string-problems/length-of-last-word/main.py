# initial solution
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        for i in reversed(s.split(' ')):
            if i:
                return len(i)
        return 0
