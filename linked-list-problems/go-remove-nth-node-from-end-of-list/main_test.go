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

func Test_removeNthFromEnd(t *testing.T) {
	t.Parallel()
	type args struct {
		head []int
		n    int
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
				n:    2,
			},
			want: []int{1, 2, 3, 5},
		},
		{
			name: "example 2",
			args: args{
				head: []int{1},
				n:    1,
			},
			want: []int{},
		},
		{
			name: "example 3",
			args: args{
				head: []int{1, 2},
				n:    1,
			},
			want: []int{1},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			t.Parallel()
			if got := removeNthFromEnd(sliceToList(tt.args.head), tt.args.n); !reflect.DeepEqual(listToSlice(got), tt.want) {
				t.Errorf("removeNthFromEnd() = %v, want %v", got, tt.want)
			}
		})
	}
}
