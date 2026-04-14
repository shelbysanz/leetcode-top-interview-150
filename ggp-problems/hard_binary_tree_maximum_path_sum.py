# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # keep track of max sum
        max_sum = float('-inf')

        # dfs to get max path value
        def dfs(node):
            if not node:
                return 0

            nonlocal max_sum

            left_sum = max(dfs(node.left), 0)
            right_sum = max(dfs(node.right), 0)

            max_sum = max(max_sum, left_sum + right_sum + node.val)
            return max(max(left_sum, right_sum) + node.val, node.val)

        dfs(root)

        # constraints guarantee atleast one node so max_sum should never be -inf or a float we can raise an exception to ensure this
        if isinstance(max_sum, float):
            raise Exception('This function should never be called with an empty root node')

        # return max sum
        return max_sum
