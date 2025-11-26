class Solution:
    def reverseBits(self, n: int) -> int:
        binary_repr = bin(n)[2:].zfill(32)
        start, end = 0, len(binary_repr) - 1
        arr: list[str] = [""] * len(binary_repr)
        while start < end:
            arr[start], arr[end] = binary_repr[end], binary_repr[start]
            start += 1
            end -= 1
        reversed_bin = "".join(arr)
        return int(reversed_bin, 2)
