class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow = head
        fast = head.next

        while fast:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next if fast.next else None
        return False
