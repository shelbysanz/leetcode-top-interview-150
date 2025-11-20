class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashmap: dict[str, list[str]] = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in hashmap:
                hashmap[sorted_s] = []
            hashmap[sorted_s].append(s)
        ret: list[list[str]] = []
        for _, val in hashmap.items():
            ret.append(val)
        return ret
