package leetcode

func rangeBitwiseAnd(left int, right int) int {
	var shift int
	for left < right {
		left >>= 1
		right >>= 1
		shift++
	}
	return left << shift
}
