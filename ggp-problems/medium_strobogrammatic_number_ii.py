class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        pairs = [("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")]

        ans = []
        arr = [""] * n

        def recurse(left, right):
            if left > right:
                ans.append("".join(arr))
                return

            for a, b in pairs:
                # no leading 0s
                if left == 0 and n != 1 and a == "0":
                    continue

                # handle middle digits
                if left == right and a != b:
                    continue

                # set and recurse
                arr[left] = a
                arr[right] = b

                recurse(left + 1, right - 1)

        recurse(0, n - 1)
        return ans
