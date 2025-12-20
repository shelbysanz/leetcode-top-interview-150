package leetcode

import (
	"reflect"
	"testing"
)

func Test_letterCombinations(t *testing.T) {
	t.Parallel()
	type args struct {
		digits string
	}
	tests := []struct {
		name string
		args args
		want []string
	}{
		{
			name: "example 1",
			args: args{
				digits: "23",
			},
			want: []string{"ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"},
		},
		{
			name: "example 2",
			args: args{
				digits: "2",
			},
			want: []string{"a", "b", "c"},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			t.Parallel()
			if got := letterCombinations(tt.args.digits); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("letterCombinations() = %v, want %v", got, tt.want)
			}
		})
	}
}
