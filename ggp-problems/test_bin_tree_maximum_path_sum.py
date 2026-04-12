class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfsSum(node: TreeNode | None):
    if not node:
        return float("-inf")

    if not node.left and not node.right:  # means its a leaf
        return node.val

    left_sum = dfsSum(node.left)
    right_sum = dfsSum(node.right)

    return node.val + max(left_sum, right_sum)


def maxRootToLeafSum(root: TreeNode | None):
    # base case
    if root is None:
        return root

    return dfsSum(root)


# Test 1 — Basic Tree
root1 = TreeNode(1, TreeNode(2), TreeNode(3))

# Test 2 — Deeper Left Path
root2 = TreeNode(1, TreeNode(2, TreeNode(10)), TreeNode(3))

# Test 3 — Negatives
root3 = TreeNode(-10, TreeNode(-20), TreeNode(-3))

# Test 4 — Single Node
root4 = TreeNode(7)

# Test 5 — One-Sided Tree
root5 = TreeNode(5, TreeNode(2))

# Test 6 — Mixed Values
root6 = TreeNode(5, TreeNode(4, TreeNode(-11)), TreeNode(8, TreeNode(13), TreeNode(4)))

tests = [
    (root1, 4),
    (root2, 13),
    (root3, -13),
    (root4, 7),
    (root5, 7),
    (root6, 26),
]

for i, (root, expected) in enumerate(tests, 1):
    result = maxRootToLeafSum(root)
    status = "PASS" if result == expected else "FAIL"
    print(f"Test {i}")
    print(f"  Result:   {result}")
    print(f"  Expected: {expected}")
    print(f"  Status:   {status}")
    print("-" * 30)
