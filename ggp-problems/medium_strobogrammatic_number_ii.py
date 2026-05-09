def isStrobogrammatic(num: str) -> bool:
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


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        nums = ["0", "1", "6", "8", "9"]

        ans = []

        def recurse(curr):
            if len(curr) == n:
                if curr[0] != "0" or n == 1:
                    if isStrobogrammatic(curr):
                        ans.append(curr)
                return

            for digit in nums:
                recurse(curr + digit)

        recurse("")
        return ans
