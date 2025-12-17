package leetcode

/**
 * Definition for singly-linked list.
 */

type ListNode struct {
    Val int
    Next *ListNode
}

func partition(head *ListNode, x int) *ListNode {
	lt_head := &ListNode{}
	gte_head := &ListNode{}
	lt := lt_head
	gte := gte_head
	for head != nil {
		tmp := head.Next
		head.Next = nil
		if head.Val < x {
			lt.Next = head
			lt = lt.Next
		} else {
			gte.Next = head
			gte = gte.Next
		}
		head = tmp
	}
	lt.Next = gte_head.Next
    return lt_head.Next
}
