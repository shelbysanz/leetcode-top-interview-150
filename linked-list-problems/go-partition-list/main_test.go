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

func Test_partition(t *testing.T) {
	t.Parallel()
	type args struct {
		head []int
		x    int
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		{
			name: "example 1",
			args: args{
				head: []int{1, 4, 3, 2, 5, 2},
				x:    3,
			},
			want: []int{1, 2, 2, 4, 3, 5},
		},
		{
			name: "example 2",
			args: args{
				head: []int{2, 1},
				x:    2,
			},
			want: []int{1, 2},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			t.Parallel()
			if got := partition(sliceToList(tt.args.head), tt.args.x); !reflect.DeepEqual(listToSlice(got), tt.want) {
				t.Errorf("partition() = %v, want %v", listToSlice(got), tt.want)
			}
		})
	}
}
