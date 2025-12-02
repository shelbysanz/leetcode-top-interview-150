# Leetcode's definition for a binary tree node.
class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val: int = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right

