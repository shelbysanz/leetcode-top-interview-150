from ..TreeNode import TreeNode


class Solution:
    def getMinimumDifference(self, root: TreeNode | None) -> int:
        min_diff = float("inf")
        stack: list[TreeNode] = []
        curr: TreeNode | None = root
        prev = None
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if prev is not None:
                min_diff = min(min_diff, abs(prev - curr.val))
                if min_diff == 1:
                    return 1
            prev = curr.val
            curr = curr.right
        return int(min_diff)
