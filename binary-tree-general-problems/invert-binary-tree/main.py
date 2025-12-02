from ..TreeNode import TreeNode
from collections import deque


class Solution:
    def invertTree(self, root: TreeNode | None = None) -> TreeNode | None:
        if root is None:
            return None
        new_root = TreeNode(val=root.val)
        queue = deque([root])
        new_queue = deque([new_root])
        while queue and new_queue:
            node = queue.popleft()
            new_node = new_queue.popleft()

            if node.right is not None:
                new_node.left = TreeNode(val=node.right.val)
                queue.append(node.right)
                new_queue.append(new_node.left)
            else:
                new_node.left = None

            if node.left is not None:
                new_node.right = TreeNode(val=node.left.val)
                queue.append(node.left)
                new_queue.append(new_node.right)
            else:
                new_node.right = None
        return new_root
