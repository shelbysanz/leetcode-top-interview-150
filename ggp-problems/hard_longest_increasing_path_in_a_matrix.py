class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        memo = [[0] * cols for _ in range(rows)]

        def backtracking(x, y):
            if memo[x][y]:
                return memo[x][y]

            l, r, t, b = (
                max(0, y - 1),
                min(cols - 1, y + 1),
                max(0, x - 1),
                min(rows - 1, x + 1),
            )
            best = 1
            for xi, yi in [(x, l), (x, r), (t, y), (b, y)]:
                if matrix[xi][yi] > matrix[x][y]:
                    path_len = backtracking(xi, yi)
                    best = max(best, path_len + 1)
            memo[x][y] = best
            return best

        max_len = 0
        for row in range(rows):
            for col in range(cols):
                max_len = max(max_len, backtracking(row, col))

        return max_len
