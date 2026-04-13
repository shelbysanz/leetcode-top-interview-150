# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        # initialize fast pointer
        fast = head
        for _ in range(n):
            fast = fast.next

        # traverse one by one
        slow = dummy
        while fast:
            fast = fast.next
            slow = slow.next

        # when fast reaches end slow will be at the node we want to update
        # update slow.next to be slow.next.next
        slow.next = slow.next.next

        # return the head
        return dummy.next
