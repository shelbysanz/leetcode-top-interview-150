from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        queue = deque([root])
        ret = []
        while queue:
            node = queue.popleft()
            if node is None:
                ret.append("None")
                continue
            ret.append(str(node.val))

            queue.append(node.left)
            queue.append(node.right)

        while ret and ret[-1] == "None":
            ret.pop()

        return ",".join(ret)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        vals = data.split(",")

        root = TreeNode(vals[0])
        queue = deque([root])
        i = 1
        while queue and i < len(vals):
            node = queue.popleft()

            if vals[i] != "None":
                node.left = TreeNode(vals[i])
                queue.append(node.left)
            i += 1

            if i < len(vals) and vals[i] != "None":
                node.right = TreeNode(vals[i])
                queue.append(node.right)
            i += 1

        return root
