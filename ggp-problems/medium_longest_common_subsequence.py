class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1) # rows
        m = len(text2) # cols

        # initialize dp (+ 1 due to boundaries)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        # bottoms up approach
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])

        # dp[0][0] will have the int with largest common substring
        return dp[0][0]
