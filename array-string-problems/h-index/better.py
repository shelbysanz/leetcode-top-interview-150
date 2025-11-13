class Solution:
    def hIndex(self, citations: list[int]) -> int:
        l = len(citations)
        buckets: list[int] = [0] * (l + 1)

        for i in citations:
            if i >= l:
                buckets[l] += 1
            else:
                buckets[i] += 1

        total = 0
        for i in range(l, -1, -1):
            total += buckets[i]
            if total >= i:
                return i
        return 0


if __name__ == "__main__":
    assert Solution().hIndex([3,0,6,1,5]) == 3
