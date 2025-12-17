package leetcode

func copyRandomList2(head *Node) *Node {
	nodeMap := make(map[*Node]*Node)

	node := head
	// copy the nodes
	for node != nil {
		nodeMap[node] = &Node{Val: node.Val}
		node = node.Next
	}

	node = head
	// wire the random and next pointers
	for node != nil {
		nodeMap[node].Next = nodeMap[node.Next]
		nodeMap[node].Random = nodeMap[node.Random]
		node = node.Next
	}
	return nodeMap[head]
}
