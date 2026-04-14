class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        left, right = 0, len(num) - 1

        map = {
            "0": "0",
            "1": "1",
            "2": None,
            "3": None,
            "4": None,
            "5": None,
            "6": "9",
            "7": None,
            "8": "8",
            "9": "6",
        }

        while left <= right:
            mapped = map[num[left]]
            if mapped != num[right]:
                return False
            left += 1
            right -= 1

        return True
