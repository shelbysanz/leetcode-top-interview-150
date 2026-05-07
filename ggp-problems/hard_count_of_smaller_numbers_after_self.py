class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        values = sorted(set(nums))
        rank_map = {v: i + 1 for i, v in enumerate(values)}
        fenwick = [0] * (len(values) + 1)
        output = [0] * len(nums)

        def update(i):
            while i < len(fenwick):
                fenwick[i] += 1
                i += i & -i

        def query(i):
            total = 0
            while i > 0:
                total += fenwick[i]
                i -= i & -i
            return total

        for i in range(len(nums) - 1, -1, -1):
            rank = rank_map[nums[i]]
            output[i] = query(rank - 1)
            update(rank)

        return output
