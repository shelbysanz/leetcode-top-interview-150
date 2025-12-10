from ..TreeNode import TreeNode
from collections import deque


class Solution:
    def rightSideView(self, root: TreeNode | None = None) -> list[int]:
        if root is None:
            return []
        levels: list[int] = []
        queue = deque([root])
        while queue:
            len_q = len(queue)
            for i in range(len_q):
                node = queue.popleft()
                if i == len_q - 1:
                    levels.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return levels
