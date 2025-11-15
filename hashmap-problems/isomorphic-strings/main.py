class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        t_to_s_hashmap: dict[str, str] = {}
        s_to_t_hashmap: dict[str, str] = {}

        for s_char, t_char in zip(s, t):
            s_val = t_to_s_hashmap.get(t_char, None)
            t_val = s_to_t_hashmap.get(s_char, None)
            if (s_val is not None or t_val is not None) and (s_val != s_char or t_val != t_char):
                return False
            if s_val is None and t_val is None:
                t_to_s_hashmap[t_char] = s_char
                s_to_t_hashmap[s_char] = t_char
        return True


if __name__ == "__main__":
    assert Solution().isIsomorphic("foo", "bar") == False
    assert Solution().isIsomorphic("egg", "add") == True
    assert Solution().isIsomorphic("paper", "title") == True
