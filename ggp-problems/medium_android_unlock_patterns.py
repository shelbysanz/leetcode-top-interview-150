class Solution:
    def __init__(self):
        self.skip = [[0] * 10 for _ in range(10)]
        self.skip[1][3] = self.skip[3][1] = 2
        self.skip[1][7] = self.skip[7][1] = 4
        self.skip[3][9] = self.skip[9][3] = 6
        self.skip[7][9] = self.skip[9][7] = 8
        self.skip[1][9] = self.skip[9][1] = 5
        self.skip[2][8] = self.skip[8][2] = 5
        self.skip[3][7] = self.skip[7][3] = 5
        self.skip[4][6] = self.skip[6][4] = 5

    def numberOfPatterns(self, m: int, n: int) -> int:
        def dfs(vis, skip, cur, remain):
            if remain < 0:
                return 0
            if remain == 0:
                return 1
            vis[cur] = 1
            res = 0
            for i in range(1, 10):
                if not vis[i] and (skip[cur][i] == 0 or vis[skip[cur][i]]):
                    res += dfs(vis, skip, i, remain - 1)
            vis[cur] = 0
            return res

        vis = [0] * 10
        res = 0
        for i in range(m, n + 1):
            res += dfs(vis, self.skip, 1, i - 1) * 4
            res += dfs(vis, self.skip, 2, i - 1) * 4
            res += dfs(vis, self.skip, 5, i - 1)
        return res
