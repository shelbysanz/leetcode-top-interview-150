from collections import defaultdict


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        target_node = len(graph) - 1
        adj = defaultdict(list)
        for i, nodes in enumerate(graph):
            adj[i].extend(nodes)

        def dfs(node, path):
            if node == target_node:
                paths.append(path[:])
                return
            for u in adj[node]:
                path.append(u)
                dfs(u, path)
                path.pop()

        dfs(0, [0])
        return paths
