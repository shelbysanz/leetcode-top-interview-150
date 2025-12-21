from collections import deque


class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        flattened_board: list[int] = []
        left_to_right = True
        for row in reversed(board):
            cols = row if left_to_right else reversed(row)
            for c in cols:
                flattened_board.append(c)
            left_to_right = not left_to_right
        queue = deque([(0, 0)])
        visited = {0}
        while queue:
            pos, steps = queue.popleft()
            if pos == len(flattened_board) - 1:
                return steps
            for move in range(1, 7):
                next_pos = pos + move
                if next_pos >= len(flattened_board):
                    continue
                square = (
                    flattened_board[next_pos] - 1
                    if flattened_board[next_pos] != -1
                    else next_pos
                )
                if square not in visited:
                    visited.add(square)
                    queue.append((square, steps + 1))
        return -1
