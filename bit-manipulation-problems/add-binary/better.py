class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not a or not b:
            return a + b
        a_index, b_index = len(a) - 1, len(b) - 1
        result: list[int] = []
        carry = 0
        while a_index >= 0 or b_index >= 0:
            a_val = a[a_index] if a_index >= 0 else '0'
            b_val = b[b_index] if b_index >= 0 else '0'
            sum = int(a_val) + int(b_val) + carry
            result.append(sum % 2)
            carry = sum // 2
            if a_index >= 0:
                a_index -= 1
            if b_index >= 0:
                b_index -= 1
        if carry:
            result.append(carry)
        return "".join(str(i) for i in reversed(result))
