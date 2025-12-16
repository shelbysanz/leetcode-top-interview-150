package leetcode

/**
 * Leetcode's definition for a Node.
 */

type Node struct {
	Val    int
	Next   *Node
	Random *Node
}

func copyRandomList(head *Node) *Node {
	if head == nil {
		return nil
	}
	// interweave copy nodes
	node := head
	for node != nil {
		next_original := node.Next
		node.Next = &Node{Val: node.Val, Next: next_original}
		node = next_original
	}
	// add random pointers to keep track of copies
	node = head
	for node != nil {
		if node.Random != nil {
			node.Next.Random = node.Random.Next
		}
		node = node.Next.Next
	}
	// separate original and copy lists
	original := head
	copy_head := head.Next
	for original != nil {
		copy := original.Next
		original.Next = copy.Next
		if copy.Next != nil {
			copy.Next = copy.Next.Next
		}
		original = original.Next
	}
	return copy_head
}
