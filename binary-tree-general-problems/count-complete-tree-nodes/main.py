from typing import Callable
from ..TreeNode import TreeNode


class Solution:
    def countNodes(self, root: TreeNode | None = None) -> int:
        if root is None:
            return 0

        def get_height(
            node: TreeNode | None, get_node: Callable[[TreeNode], TreeNode | None]
        ) -> int:
            height: int = 0
            while node:
                height += 1
                node = get_node(node)
            return height

        def count_nodes(node: TreeNode | None = None) -> int:
            if node is None:
                return 0

            left_height = get_height(node, lambda x: x.left)
            right_height = get_height(node, lambda x: x.right)

            if left_height == right_height:
                return (1 << left_height) - 1
            else:
                return 1 + count_nodes(node.left) + count_nodes(node.right)

        return count_nodes(root)
