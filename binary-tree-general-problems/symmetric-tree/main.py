from ..TreeNode import TreeNode
from collections import deque


class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if root is None:
            return True
        if (root.left is None) != (root.right is None):
            return False
        if root.left is not None and root.right is not None:
            left_queue = deque([root.left])
            right_queue = deque([root.right])
            while left_queue and right_queue:
                left_node = left_queue.popleft()
                right_node = right_queue.popleft()
                if left_node.val != right_node.val:
                    return False
                if ((left_node.left is None) != (right_node.right is None)) or (
                    (left_node.right is None) != (right_node.left is None)
                ):
                    return False
                if left_node.left and right_node.right:
                    left_queue.append(left_node.left)
                    right_queue.append(right_node.right)
                if left_node.right and right_node.left:
                    left_queue.append(left_node.right)
                    right_queue.append(right_node.left)
        return True
