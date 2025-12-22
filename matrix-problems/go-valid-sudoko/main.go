package leetcode

func isValidSudoku(board [][]byte) bool {
	rows := make([]map[byte]bool, 9)
	cols := make([]map[byte]bool, 9)
	boxes := make([]map[byte]bool, 9)

	for i := range 9 {
		rows[i] = make(map[byte]bool)
		cols[i] = make(map[byte]bool)
		boxes[i] = make(map[byte]bool)
	}

	for r_idx, row := range board {
		for c_idx, val := range row {
			if val == '.' {
				continue
			}
			// check box
			box_index := (r_idx/3)*3 + (c_idx / 3)
			if _, exists := boxes[box_index][val]; exists {
				return false
			} else {
				boxes[box_index][val] = true
			}
			// check rows
			if _, exists := rows[r_idx][val]; exists {
				return false
			} else {
				rows[r_idx][val] = true
			}
			// check cols
			if _, exists := cols[c_idx][val]; exists {
				return false
			} else {
				cols[c_idx][val] = true
			}
		}
	}

	return true
}
