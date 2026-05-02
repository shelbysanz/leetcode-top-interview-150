class DisjointSet:
    def __init__(self):
        self.parent = {}
        self.size = {}

    def find_parent(self, u):
        if u not in self.parent:
            self.parent[u] = u
            self.size[u] = 1
            return u

        if self.parent[u] == u:
            return u

        self.parent[u] = self.find_parent(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        ul_par_u = self.find_parent(u)
        ul_par_v = self.find_parent(v)

        if ul_par_u == ul_par_v:
            return

        if self.size[ul_par_u] > self.size[ul_par_v]:
            self.parent[ul_par_v] = ul_par_u
            self.size[ul_par_u] += self.size[ul_par_v]
        else:
            self.parent[ul_par_u] = ul_par_v
            self.size[ul_par_v] += self.size[ul_par_u]


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        offset = max(row for row, col in stones) + 1

        ds = DisjointSet()

        seen = set()
        for row, col in stones:
            col += offset
            ds.union(row, col)
            seen.add(row)
            seen.add(col)

        components = set()
        for node in seen:
            components.add(ds.find_parent(node))

        return len(stones) - len(components)
