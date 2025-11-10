class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap: dict[str, int] = {}
        for i in magazine:
            hashmap[i] = hashmap.get(i, 0) + 1
        for i in ransomNote:
            if hashmap.get(i) is None or hashmap.get(i) == 0:
                return False
            hashmap[i] -= 1
        return True
