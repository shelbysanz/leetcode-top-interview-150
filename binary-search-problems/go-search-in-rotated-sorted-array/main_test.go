package leetcode

import "testing"

func Test_search(t *testing.T) {
	t.Parallel()
	type args struct {
		nums   []int
		target int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "example 1",
			args: args{
				nums:   []int{4, 5, 6, 7, 0, 1, 2},
				target: 0,
			},
			want: 4,
		},
		{
			name: "example 2",
			args: args{
				nums:   []int{4, 5, 6, 7, 0, 1, 2},
				target: 3,
			},
			want: -1,
		},
		{
			name: "example 3",
			args: args{
				nums:   []int{1},
				target: 0,
			},
			want: -1,
		},
		{
			name: "valid input",
			args: args{
				nums:   []int{1, 2, 3, 4, 5},
				target: 3,
			},
			want: 2,
		},
		{
			name: "edge case empty",
			args: args{
				nums:   []int{},
				target: 0,
			},
			want: -1,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			t.Parallel()
			if got := search(tt.args.nums, tt.args.target); got != tt.want {
				t.Errorf("search() = %v, want %v", got, tt.want)
			}
		})
	}
}
