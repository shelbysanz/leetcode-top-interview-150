class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        nodes = []
        def dfs(node):
            if node.left:
                dfs(node.left)
            nodes.append(node.val)
            if node.right:
                dfs(node.right)
        dfs(root)
        return nodes
