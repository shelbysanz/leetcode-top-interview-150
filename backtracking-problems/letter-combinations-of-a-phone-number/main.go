package leetcode

func letterCombinations(digits string) []string {
	numberMap := map[byte][]byte{
		'2': {'a', 'b', 'c'},
		'3': {'d', 'e', 'f'},
		'4': {'g', 'h', 'i'},
		'5': {'j', 'k', 'l'},
		'6': {'m', 'n', 'o'},
		'7': {'p', 'q', 'r', 's'},
		'8': {'t', 'u', 'v'},
		'9': {'w', 'x', 'y', 'z'},
	}

	results := []string{}
	var backtrack func(index int, curr_str string)
	backtrack = func(index int, curr_str string) {
		if index == len(digits) {
			results = append(results, curr_str)
			return
		}

		digit := digits[index]
		letters := numberMap[digit]
		for _, letter := range letters {
			backtrack(index+1, curr_str+string(letter))
		}
	}

	if len(digits) > 0 {
		backtrack(0, "")
	}

	return results
}
