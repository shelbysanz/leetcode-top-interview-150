# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # get height
        def getHeight(node, getNextNode):
            height = 0
            while node:
                height += 1
                node = getNextNode(node)
            return height

        # recursive get count
        def count(node):
            # base case no node
            if not node:
                return 0

            # get dfs height leftmost and rightmost
            left_height = getHeight(node, lambda node: node.left)
            right_height = getHeight(node, lambda node: node.right)
            # case 1: the heights are the same
            if left_height == right_height:
                # node count is 2^h - 1 (so we don't count the root twice)
                return 2 ** left_height - 1
            # case 2: left > right
            else:
                # node count is the count of the left and count of the right + 1 for the root
                return count(node.left) + count(node.right) + 1

        # run count on the root
        return count(root)
