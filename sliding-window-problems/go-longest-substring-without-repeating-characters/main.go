package leetcode

func lengthOfLongestSubstring(s string) int {
	lookup := make(map[byte]int)
	start := 0
	maxLength := 0
	for end := 0; end < len(s); end++ {
		index, found := lookup[s[end]]
		if found && index >= start {
			start = index + 1
		}
		lookup[s[end]] = end
		currLen := end - start + 1
		maxLength = max(maxLength, currLen)
	}
	return maxLength
}
