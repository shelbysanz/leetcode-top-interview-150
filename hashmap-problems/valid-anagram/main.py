class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_hashmap: dict[str, int] = {}
        t_hashmap: dict[str, int] = {}
        for i in range(0, len(s)):
            s_hashmap[s[i]] = s_hashmap.get(s[i], 0) + 1
            t_hashmap[t[i]] = t_hashmap.get(t[i], 0) + 1
        return s_hashmap == t_hashmap
