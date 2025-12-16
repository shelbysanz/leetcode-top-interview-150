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

func Test_addTwoNumbers(t *testing.T) {
	t.Parallel()
	type args struct {
		l1 []int
		l2 []int
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		{
			name: "example 1",
			args: args{
				l1: []int{2, 4, 3},
				l2: []int{5, 6, 4},
			},
			want: []int{7, 0, 8},
		},
		{
			name: "example 2",
			args: args{
				l1: []int{0},
				l2: []int{0},
			},
			want: []int{0},
		},
		{
			name: "example 3",
			args: args{
				l1: []int{9, 9, 9, 9, 9, 9, 9},
				l2: []int{9, 9, 9, 9},
			},
			want: []int{8, 9, 9, 9, 0, 0, 0, 1},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			t.Parallel()
			if got := addTwoNumbers(sliceToList(tt.args.l1), sliceToList(tt.args.l2)); !reflect.DeepEqual(listToSlice(got), tt.want) {
				t.Errorf("addTwoNumbers() = %v, want %v", got, tt.want)
			}
		})
	}
}
