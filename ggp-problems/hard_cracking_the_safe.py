class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        seen, ans = set(), []

        def dfs(node):
            for digit in range(k):
                u = node + str(digit)

                if u not in seen:
                    seen.add(u)
                    dfs(u[1:])
                    ans.append(str(digit))

        start = "0" * (n - 1)
        dfs(start)
        return "".join(ans) + start
