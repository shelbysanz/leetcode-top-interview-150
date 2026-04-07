package leetcode

/**
 * Definition for singly-linked list.
 */

type ListNode struct {
	Val  int
	Next *ListNode
}

func splitList(node *ListNode) (*ListNode, *ListNode) {
	root := node
	slow := node
	fast := node
	var prev *ListNode = nil
	for fast != nil && fast.Next != nil {
		prev = slow
		slow = slow.Next
		fast = fast.Next.Next
	}
	if prev != nil {
		prev.Next = nil
	}
	return root, slow
}

func merge(left *ListNode, right *ListNode) *ListNode {
	var root *ListNode = &ListNode{}
	var node *ListNode = root
	for left != nil && right != nil {
		if left.Val < right.Val {
			node.Next = left
			left = left.Next
			node = node.Next
		} else {
			node.Next = right
			right = right.Next
			node = node.Next
		}
	}
	if left != nil {
		node.Next = left
	} else if right != nil {
		node.Next = right
	}
	return root.Next
}

func sort(node *ListNode) *ListNode {
	if node == nil || node.Next == nil {
		return node
	}

	left, right := splitList(node)

	sorted_left := sort(left)
	sorted_right := sort(right)

	return merge(sorted_left, sorted_right)
}

func sortList(head *ListNode) *ListNode {
	return sort(head)
}
