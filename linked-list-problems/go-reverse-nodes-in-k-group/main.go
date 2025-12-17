package leetcode

/**
 * Definition for singly-linked list.
 */

type ListNode struct {
	Val  int
	Next *ListNode
}

func countNodes(node *ListNode) int {
	count := 0
	for node != nil {
		count++
		node = node.Next
	}
	return count
}

func reverseKGroup(head *ListNode, k int) *ListNode {
	head = &ListNode{Next: head}
	groups := countNodes(head.Next) / k

	prev := head
	first := head.Next
	for range groups {
		for i := 1; i < k; i++ {
			tmp := first.Next
			first.Next = tmp.Next
			tmp.Next = prev.Next
			prev.Next = tmp
		}
		prev = first
		first = prev.Next
	}
	return head.Next
}
