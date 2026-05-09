class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        total = k**n
        seen = set()

        def dfs(curr):
            if curr[-n:] in seen:
                return
            seen.add(curr[-n:])

            if len(seen) == total:
                return curr
            for i in range(k):
                pswd = dfs(curr + str(i))
                if pswd:
                    return pswd
            seen.remove(curr[-n:])

        return dfs("0" * n)
