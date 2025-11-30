# Definition for a binary tree node.
class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val: int = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


class Solution:
    def maxDepth(self, root: TreeNode | None = None) -> int:
        def getNodeDepth(node: TreeNode | None = None) -> int:
            if node is None:
                return 0
            left: int = getNodeDepth(node.left) if node.left is not None else 0
            right: int = getNodeDepth(node.right) if node.right is not None else 0
            return 1 + max(left, right)

        return getNodeDepth(root)
