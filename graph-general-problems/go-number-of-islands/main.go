package leetcode

func numIslands(grid [][]byte) int {
	if grid == nil || grid[0] == nil {
		return 0
	}
	island_count := 0
	rows, cols := len(grid), len(grid[0])

	var search func(r, c int)
	search = func(r, c int) {
		if r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] != '1' {
			return
		}

		// mark visited
		grid[r][c] = '0'

		search(r+1, c)
		search(r-1, c)
		search(r, c+1)
		search(r, c-1)
	}

	for range rows {
		for range cols {
			if grid[r]
		}
	}
	return island_count
}
