from ..TreeNode import TreeNode


class Solution:
    def isSameTree(self, p: TreeNode | None = None, q: TreeNode | None = None) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        p_queue = [p]
        q_queue = [q]
        while p_queue or q_queue:
            p_node = p_queue.pop(0)
            q_node = q_queue.pop(0)
            if p_node.val != q_node.val:
                return False
            if (p_node.left is None) != (q_node.left is None):
                return False
            if p_node.left and q_node.left:
                p_queue.append(p_node.left)
                q_queue.append(q_node.left)
            if (p_node.right is None) != (q_node.right is None):
                return False
            if p_node.right and q_node.right:
                p_queue.append(p_node.right)
                q_queue.append(q_node.right)
        return not p_queue and not q_queue
