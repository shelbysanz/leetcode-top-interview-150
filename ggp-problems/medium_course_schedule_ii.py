from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [i for i in range(numCourses)]

        topo_stack = []
        vis = [0] * numCourses

        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[u].append(v)

        def dfs(u):
            if vis[u] == 1:
                return False
            if vis[u] == 2:
                return True

            vis[u] = 1
            for v in adj[u]:
                if not dfs(v):
                    return False
            vis[u] = 2
            topo_stack.append(u)
            return True

        for u in range(len(vis)):
            if not dfs(u):
                return []

        return topo_stack
