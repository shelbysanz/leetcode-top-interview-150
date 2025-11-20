class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashmap: dict[tuple[int,...], list[str]] = {}
        for s in strs:
            char_count = [0] * 26
            for i in s:
                char_count[ord(i) - ord('a')] += 1
            key = tuple(char_count)
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(s)
        results: list[list[str]] = []
        for key, val in hashmap.items():
            results.append(val)
        return results
