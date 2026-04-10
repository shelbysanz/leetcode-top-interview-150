class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()
        n = len(s)
        plate = []
        for i in range(n - 1, -1, -k):
            starting = max(i-k+1, 0)
            plate.append(s[starting:i+1])
        return '-'.join(reversed(plate))
