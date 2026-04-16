class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        # leetcode guarantees atleast length 1
        # base case
        max_p_range = [0, 1]
        max_p_count = 1

        def expand(curr_count, l, r):
            nonlocal max_p_count
            nonlocal max_p_range

            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                curr_count += 2
                if curr_count > max_p_count:
                    max_p_count = curr_count
                    max_p_range = [l, r + 1]
                l -= 1
                r += 1

        for i in range(n):
            # odd palindromes
            curr_count = 1
            l, r = i - 1, i + 1
            expand(curr_count, l, r)

            # even palindromes
            if i + 1 >= n:
                continue
            if s[i] != s[i + 1]:
                continue
            curr_count = 0
            l, r = i, i + 1
            expand(curr_count, l, r)

        return s[max_p_range[0] : max_p_range[1]]

