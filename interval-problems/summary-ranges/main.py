class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []

        result: list[str] = []
        range_start = nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] + 1 != nums[i]:
                if range_start == nums[i-1]:
                    result.append(f"{nums[i-1]}")
                    range_start = nums[i]
                else:
                    result.append(f"{range_start}->{nums[i-1]}")
                    range_start = nums[i]

        if range_start == nums[-1]:
            result.append(f"{range_start}")
        else:
            result.append(f"{range_start}->{nums[-1]}")
        return result