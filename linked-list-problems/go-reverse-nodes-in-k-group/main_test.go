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

func Test_reverseKGroup(t *testing.T) {
	t.Parallel()
	type args struct {
		head []int
		k    int
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		{
			name: "example 1",
			args: args{
				head: []int{1, 2, 3, 4, 5},
				k:    2,
			},
			want: []int{2, 1, 4, 3, 5},
		},
		{
			name: "example 2",
			args: args{
				head: []int{1, 2, 3, 4, 5},
				k:    3,
			},
			want: []int{3, 2, 1, 4, 5},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			t.Parallel()
			if got := reverseKGroup(sliceToList(tt.args.head), tt.args.k); !reflect.DeepEqual(listToSlice(got), tt.want) {
				t.Errorf("reverseKGroup() = %v, want %v", got, tt.want)
			}
		})
	}
}
