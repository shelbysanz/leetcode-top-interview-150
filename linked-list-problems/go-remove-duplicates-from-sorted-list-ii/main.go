package leetcode

/**
 * Definition for singly-linked list.
 */

type ListNode struct {
	Val  int
	Next *ListNode
}

func deleteDuplicates(head *ListNode) *ListNode {
	head = &ListNode{Next: head}
	node := head
	for node.Next != nil && node.Next.Next != nil {
		start := node.Next
		end := start.Next
		if start.Val == end.Val {
			for end != nil && end.Val == start.Val {
				end = end.Next
			}
			node.Next = end
		} else {
			node = node.Next
		}
	}
	return head.Next
}
