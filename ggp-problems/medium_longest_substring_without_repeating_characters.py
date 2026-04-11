from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # base case
        if len(s) <= 1:
            return len(s)

        # default dict of letters initialized at -1, initalize max_len
        letters = defaultdict(lambda: -1)  # default value is -1 represents index
        max_len = 0

        start = 0
        # for each lookup, if seen >= start update start
        for idx, val in enumerate(s):
            if letters[val] >= start:
                start = letters[val] + 1
            # calculate current length
            curr_len = idx - start + 1

            # update max if necessary
            max_len = max(max_len, curr_len)

            # update letters
            letters[val] = idx

        return max_len
