from ..TreeNode import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        def create_node(left: int, right: int) -> TreeNode | None:
            if left > right:
                return None
            mid = left + (right - left) // 2
            left_node = create_node(left, mid - 1)
            right_node = create_node(mid + 1, right)
            return TreeNode(nums[mid], left_node, right_node)

        return create_node(0, len(nums) - 1)
