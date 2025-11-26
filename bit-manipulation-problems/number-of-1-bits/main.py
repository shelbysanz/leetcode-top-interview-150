class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_repr = bin(n)[2:]
        count = 0
        for i in binary_repr:
            if i != "0":
                count += 1
        return count
