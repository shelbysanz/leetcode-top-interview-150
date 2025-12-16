package leetcode

/**
 * Leetcode's definition for singly-linked list.
 */

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	var carry int
	head := &ListNode{}
	result := head
	for l1 != nil || l2 != nil || carry != 0 {
		l1_val, l2_val := 0, 0

		if l1 != nil {
			l1_val = l1.Val
			l1 = l1.Next
		}

		if l2 != nil {
			l2_val = l2.Val
			l2 = l2.Next
		}

		val_sum := l1_val + l2_val + carry
		result.Next = &ListNode{Val: val_sum % 10}
		result = result.Next
		carry = val_sum / 10
	}
	return head.Next
}
