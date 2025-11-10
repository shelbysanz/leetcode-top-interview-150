class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = min(strs, key=len)

        for i in strs:
            if prefix == "":
                break
            while not i.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    break
        return prefix
