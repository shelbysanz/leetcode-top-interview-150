package leetcode

import "strings"

func formatLine(words []string, lineLength, maxWidth int, lastLine bool) string {
	gaps := make([]int, len(words)-1)
	needed_space := maxWidth - lineLength
	if lastLine {
		return strings.Join(words, " ") + strings.Repeat(" ", needed_space)
	}
	if len(words) == 1 {
		return words[0] + strings.Repeat(" ", needed_space)
	}
	added_space_per_gap := needed_space / len(gaps)
	remaining_spaces := needed_space % len(gaps)
	for i := range gaps {
		gaps[i] = added_space_per_gap
		if i < remaining_spaces {
			gaps[i] += 1
		}
	}

	var line string
	for i := range words {
		if i > len(gaps)-1 {
			line += words[i]
		} else {
			line += words[i] + strings.Repeat(" ", gaps[i] + 1)
		}
	}
	return line
}

func fullJustify(words []string, maxWidth int) []string {
	result := []string{}
	current_words := []string{}
	current_line_length := 0
	for i := range words {
		added_length := len(words[i])
		if len(current_words) > 0 {
			added_length += 1
		}
		if added_length+current_line_length <= maxWidth {
			current_line_length += added_length
			current_words = append(current_words, words[i])
		} else {
			line := formatLine(current_words, current_line_length, maxWidth, false)
			result = append(result, line)
			current_line_length = len(words[i])
			current_words = []string{words[i]}
		}
	}
	if len(current_words) > 0 {
		line := formatLine(current_words, current_line_length, maxWidth, true)
		result = append(result, line)
	}

	return result
}
