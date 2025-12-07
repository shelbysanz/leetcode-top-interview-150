from ..TreeNode import TreeNode


class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        def dfs(node: TreeNode | None, path_sum: int) -> bool:
            if node is None:
                return False
            path_sum += node.val
            if node.left is None and node.right is None:
                return path_sum == targetSum
            return dfs(node.left, path_sum) or dfs(node.right, path_sum)

        return dfs(root, 0)
