package leetcode

import "testing"

func Test_singleNumber(t *testing.T) {
	t.Parallel()
	type args struct {
		nums []int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "example 1",
			args: args{
				nums: []int{2, 2, 3, 2},
			},
			want: 3,
		},
		{
			name: "example 2",
			args: args{
				nums: []int{0, 1, 0, 1, 0, 1, 99},
			},
			want: 99,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			t.Parallel()
			if got := singleNumber(tt.args.nums); got != tt.want {
				t.Errorf("singleNumber() = %v, want %v", got, tt.want)
			}
		})
	}
}
