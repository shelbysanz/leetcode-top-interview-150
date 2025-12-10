from ..TreeNode import TreeNode
from collections import deque

class Solution:
    def averageOfLevels(self, root: TreeNode | None = None) -> list[float]:
        if root is None:
            return []
        levels: list[float] = []
        queue = deque([root])
        while queue:
            len_q = len(queue)
            level_sum = 0
            for _ in range(len_q):
                node = queue.popleft()
                level_sum += node.val
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            if level_sum:
                levels.append(level_sum / len_q)
            else:
                levels.append(float(0))
        return levels
