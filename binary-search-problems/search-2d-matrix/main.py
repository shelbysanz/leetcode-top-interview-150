class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m_left, m_right = 0, len(matrix) - 1

        m_index: int | None = None
        while m_left <= m_right:
            m_mid = m_left + (m_right - m_left) // 2
            if matrix[m_mid][0] == target or matrix[m_mid][-1] == target:
                return True
            elif matrix[m_mid][0] > target:
                m_right = m_mid - 1
            elif matrix[m_mid][-1] < target:
                m_left = m_mid + 1
            else:
                m_index = m_mid
                break

        if m_index is None:
            return False

        row = matrix[m_index]
        r_left, r_right = 0, len(row) - 1
        while r_left <= r_right:
            r_mid = r_left + (r_right - r_left) // 2
            if row[r_mid] == target:
                return True
            elif row[r_mid] > target:
                r_right = r_mid - 1
            elif row[r_mid] < target:
                r_left = r_mid + 1

        return False
