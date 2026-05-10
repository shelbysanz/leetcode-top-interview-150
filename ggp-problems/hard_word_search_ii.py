class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            node = trie
            for i in word:
                node = node.setdefault(i, {})
            node["#"] = word

        rows, cols = len(board), len(board[0])
        matched = []

        def backtracking(row, col, parent):
            letter = board[row][col]
            node = parent[letter]

            word_match = node.pop("#", False)
            if word_match:
                matched.append(word_match)

            board[row][col] = "#"

            for row_diff, col_diff in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                new_row, new_col = row + row_diff, col + col_diff
                if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
                    continue
                if not board[new_row][new_col] in node:
                    continue
                backtracking(new_row, new_col, node)

            board[row][col] = letter

            if not node:
                parent.pop(letter)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] in trie:
                    backtracking(row, col, trie)

        return matched
