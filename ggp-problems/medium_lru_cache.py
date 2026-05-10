class ListNode:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1

        node = self.hashmap[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.remove(node)

        node = ListNode(key=key, val=value)
        self.add(node)

        if len(self.hashmap) > self.capacity:
            node = self.head.next
            self.remove(node)

    def add(self, node):
        self.hashmap[node.key] = node

        node_before_tail = self.tail.prev
        node_before_tail.next = node
        node.prev = node_before_tail
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        del self.hashmap[node.key]

        node_before = node.prev
        node_after = node.next
        node_before.next = node_after
        node_after.prev = node_before
