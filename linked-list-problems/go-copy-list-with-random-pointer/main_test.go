package leetcode

import (
	"reflect"
	"testing"
)

// testing helpers for easy conversion
// for inputs
func sliceToNode(data [][]int) *Node {
	if len(data) == 0 {
		return nil
	}

	nodes := make([]*Node, len(data))

	// create all nodes without connecting random
	for i, d := range data {
		nodes[i] = &Node{Val: d[0]}
	}

	// set next and random pointers
	for i, d := range data {
		if i < len(data)-1 {
			nodes[i].Next = nodes[i+1]
		}
		if d[1] != -1 {
			nodes[i].Random = nodes[d[1]]
		}
	}

	return nodes[0]
}

// for outputs
func nodeToSlice(head *Node) [][]int {
	if head == nil {
		return [][]int{}
	}

	nodeList := []*Node{}
	nodeIndex := map[*Node]int{}

	// collect nodes and build index map
	curr := head
	for curr != nil {
		nodeIndex[curr] = len(nodeList)
		nodeList = append(nodeList, curr)
		curr = curr.Next
	}

	// build output
	result := make([][]int, len(nodeList))
	for i, node := range nodeList {
		rIdx := -1
		if node.Random != nil {
			rIdx = nodeIndex[node.Random]
		}
		result[i] = []int{node.Val, rIdx}
	}

	return result
}

func Test_copyRandomList(t *testing.T) {
	t.Parallel()
	type args struct {
		head [][]int
	}
	tests := []struct {
		name string
		args args
		want [][]int
	}{
		{
			name: "example 1",
			args: args{
				head: [][]int{{7, -1}, {13, 0}, {11, 4}, {10, 2}, {1, 0}},
			},
			want: [][]int{{7, -1}, {13, 0}, {11, 4}, {10, 2}, {1, 0}},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			t.Parallel()
			if got := copyRandomList1(sliceToNode(tt.args.head)); !reflect.DeepEqual(nodeToSlice(got), tt.want) {
				t.Errorf("copyRandomList() = %v, want %v", got, tt.want)
			}
			if got := copyRandomList2(sliceToNode(tt.args.head)); !reflect.DeepEqual(nodeToSlice(got), tt.want) {
				t.Errorf("copyRandomList() = %v, want %v", got, tt.want)
			}
		})
	}
}
