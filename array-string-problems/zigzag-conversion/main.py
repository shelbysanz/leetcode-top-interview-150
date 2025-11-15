class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        matrix: list[list[str]] = [[] for _ in range(numRows)]
        direction_is_down = False
        curr_row = 0
        for i in s:
            matrix[curr_row].append(i)
            if (curr_row == 0) or (curr_row == len(matrix) - 1):
                direction_is_down = not direction_is_down
            curr_row = curr_row + 1 if direction_is_down else curr_row - 1

        return "".join(''.join(i) for i in matrix)


if __name__ == "__main__":
    assert Solution().convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert Solution().convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
