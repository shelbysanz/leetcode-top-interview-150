package leetcode

/**
 * Leetcode's definition for singly-linked list.
 */

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseBetween(head *ListNode, left int, right int) *ListNode {
	if head == nil || left == right {
		return head
	}

	nodeStart := &ListNode{Next: head}
	node := nodeStart
	var prev *ListNode
	for range left {
		prev = node
		node = node.Next
	}

	reverseNode := prev.Next
	for i := 0; i < right-left; i++ {
		tmp := reverseNode.Next
		reverseNode.Next = tmp.Next
		tmp.Next = prev.Next
		prev.Next = tmp
	}

	return nodeStart.Next
}
