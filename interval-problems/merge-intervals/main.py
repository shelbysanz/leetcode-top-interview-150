class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda i: i[0])
        result: list[list[int]] = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= result[-1][1]:
                result[-1][1] = max(intervals[i][1], result[-1][1])
            else:
                result.append(intervals[i])
        return result


if __name__ == "__main__":
    print(Solution().merge([[4, 7], [1, 4]]))
