from collections import defaultdict

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        map, ret = defaultdict(list), set()
        for row in range(rows):
            for col in range(cols):
                map[board[row][col]].append((row, col))

        def backtrack(curr, coor, target, visited):
            if curr == target:
                return True
            row, col = coor
            top, bottom, left, right = (
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            )
            if top[0] >= 0 and top not in visited:
                tmp = curr + board[top[0]][top[1]]
                if tmp == target[: len(tmp)]:
                    visited.add(top)
                    if backtrack(tmp, top, target, visited):
                        return True
                    visited.remove(top)
            if bottom[0] < rows and bottom not in visited:
                tmp = curr + board[bottom[0]][bottom[1]]
                if tmp == target[: len(tmp)]:
                    visited.add(bottom)
                    if backtrack(tmp, bottom, target, visited):
                        return True
                    visited.remove(bottom)
            if left[1] >= 0 and left not in visited:
                tmp = curr + board[left[0]][left[1]]
                if tmp == target[: len(tmp)]:
                    visited.add(left)
                    if backtrack(tmp, left, target, visited):
                        return True
                    visited.remove(left)
            if right[1] < cols and right not in visited:
                tmp = curr + board[right[0]][right[1]]
                if tmp == target[: len(tmp)]:
                    visited.add(right)
                    if backtrack(tmp, right, target, visited):
                        return True
                    visited.remove(right)
            return False

        for word in words:
            start = word[0]
            for coor in map[start]:
                visited = set()
                visited.add(coor)
                if backtrack(word[0], coor, word, visited):
                    ret.add(word)
                    break

        return list(ret)
