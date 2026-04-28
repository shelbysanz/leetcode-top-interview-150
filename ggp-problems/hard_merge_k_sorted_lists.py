import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        count = 0
        for i in range(len(lists)):
            while lists[i]:
                count += 1
                heapq.heappush(heap, (lists[i].val, count , lists[i]))
                lists[i] = lists[i].next

        dummy = ListNode()
        node = dummy
        while heap:
            node.next = heapq.heappop(heap)[2]
            node = node.next
        return dummy.next
