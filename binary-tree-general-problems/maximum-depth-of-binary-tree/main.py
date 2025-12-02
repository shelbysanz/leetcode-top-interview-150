from ..TreeNode import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode | None = None) -> int:
        def getNodeDepth(node: TreeNode | None = None) -> int:
            if node is None:
                return 0
            left: int = getNodeDepth(node.left) if node.left is not None else 0
            right: int = getNodeDepth(node.right) if node.right is not None else 0
            return 1 + max(left, right)

        return getNodeDepth(root)
