package leetcode

import (
	"reflect"
	"testing"
)

// testing helpers for easy conversion
// for inputs
func sliceToList(nums []int) *ListNode {
	head := &ListNode{}
	node := head
	for _, n := range nums {
		node.Next = &ListNode{Val: n}
		node = node.Next
	}
	return head.Next
}

// for outputs
func listToSlice(head *ListNode) []int {
	result := []int{}
	for head != nil {
		result = append(result, head.Val)
		head = head.Next
	}
	return result
}

func Test_sortList(t *testing.T) {
	t.Parallel()
	type args struct {
		head []int
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		{
			name: "example 1",
			args: args{
				head: []int{4, 2, 1, 3},
			},
			want: []int{1, 2, 3, 4},
		},
		{
			name: "example 2",
			args: args{
				head: []int{-1, 5, 3, 4, 0},
			},
			want: []int{-1, 0, 3, 4, 5},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			t.Parallel()
			if got := sortList(sliceToList(tt.args.head)); !reflect.DeepEqual(listToSlice(got), tt.want) {
				t.Errorf("sortList() = %v, want %v", listToSlice(got), tt.want)
			}
		})
	}
}
