class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None
        # add a copy node beside each og node
        node = head
        while node:
            next_og = node.next
            node.next = Node(x=node.val, next=next_og)
            node = next_og

        # copy pointers
        node = head
        while node:
            copy = node.next
            copy.random = node.random.next if node.random else None
            node = copy.next

        # remove og nodes
        copy_head = head.next
        node = copy_head
        while node:
            next_copy = node.next.next if node.next else None
            node.next = next_copy
            node = node.next

        return copy_head
