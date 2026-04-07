package leetcode

/**
 * Definition for singly-linked list.
 */

type ListNode struct {
	Val  int
	Next *ListNode
}

func splitList(node *ListNode) (*ListNode, *ListNode) {
	slow, fast := node, node.Next
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}
	right := slow.Next
	slow.Next = nil
	return node, right
}

func merge(left *ListNode, right *ListNode) *ListNode {
	dummy := &ListNode{}
	tail := dummy
	for left != nil && right != nil {
		if left.Val < right.Val {
			tail.Next = left
			left = left.Next
		} else {
			tail.Next = right
			right = right.Next
		}
		tail = tail.Next
	}
	if left != nil {
		tail.Next = left
	} else {
		tail.Next = right
	}
	return dummy.Next
}

func sortList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	left, right := splitList(head)

	sorted_left := sortList(left)
	sorted_right := sortList(right)

	return merge(sorted_left, sorted_right)
}
