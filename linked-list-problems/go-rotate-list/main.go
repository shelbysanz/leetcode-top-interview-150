package leetcode

/**
 * Definition for singly-linked list.
 */

type ListNode struct {
	Val  int
	Next *ListNode
}

func countNodes(node *ListNode) (int, *ListNode) {
	count := 0
	tail := node
	for node != nil {
		count++
		tail = node
		node = node.Next
	}
	return count, tail
}

func rotateRight(head *ListNode, k int) *ListNode {
	if head == nil || head.Next == nil || k == 0 {
		return head
	}
	count, tail := countNodes(head)
	effectiveK := k % count
	if effectiveK == 0 {
		return head
	}
	// making the linked list circular
	tail.Next = head
	// rotating the list to the new tail
	stepsToTail := count - effectiveK - 1
	for range stepsToTail {
		head = head.Next
	}
	// making list no longer circular
	first := head.Next
	head.Next = nil

	return first
}
