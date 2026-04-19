class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        def rotate(i, j, temp, counter):
            next_i = j
            next_j = n - 1 - i

            next_temp = matrix[next_i][next_j]
            matrix[next_i][next_j] = temp
            if counter == 4:
                return
            counter += 1
            rotate(next_i, next_j, next_temp, counter)
        for layer in range(n // 2):
            for j in range(layer, n - 1 - layer):
                rotate(layer, j, matrix[layer][j], 0)
