class Solution:
    def intToRoman(self, num: int) -> str:
        ints = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        roman_numeral = ""
        while num > 0:
            for i in range(0, len(ints)):
                if num >= ints[i]:
                    num -= ints[i]
                    roman_numeral += romans[i]
                    break
        return roman_numeral

if __name__ == "__main__":
    assert Solution().intToRoman(58) == "LVIII"
    assert Solution().intToRoman(1994) == "MCMXCIV"
