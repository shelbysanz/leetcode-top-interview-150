# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # keep track of max path
        max_path = 0

        # for each node get the max path underneath that node
        def dfs(node):
            nonlocal max_path
            if not node:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            max_path = max(max_path, left_height + right_height)
            return max(left_height, right_height) + 1

        dfs(root)
        return max_path
