class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if len(edges) < 2:
            raise Exception("Per leetcode constraints this shouldn't happen")

        seen = set()
        nodes = edges[0] + edges[1]
        for n in nodes:
            if n in seen:
                return n
            seen.add(n)
        raise Exception("Per leetcode input specification this shouldn't happen")
