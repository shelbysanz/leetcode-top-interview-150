class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set: set[int] = set(nums)
        longest_sequence = 0
        for i in num_set:
            if i - 1 in num_set:
                continue
            number = i
            sequence_length = 1
            while number + 1 in num_set:
                sequence_length += 1
                number += 1
            longest_sequence = max(longest_sequence, sequence_length)
        return longest_sequence
