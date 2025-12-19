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

		// visit neighbor
		search(r+1, c)
		search(r-1, c)
		search(r, c+1)
		search(r, c-1)
	}

	for r := range rows {
		for c := range cols {
			if grid[r][c] == '1' {
				search(r, c)
				island_count++
			}
		}
	}
	return island_count
}
