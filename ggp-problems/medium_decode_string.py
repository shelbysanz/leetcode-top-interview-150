class Solution:
    def decodeString(self, s: str) -> str:

        def decode(n: int, encoded_str: str):
            decoded_str: str = ""
            i = 0
            while i < len(encoded_str):
                repeat_count, repeat_substr = "", ""
                while i < len(encoded_str) and encoded_str[i].isdigit():
                    repeat_count += encoded_str[i]
                    i += 1
                if encoded_str[i] == "[":
                    depth = 1
                    i += 1
                    while i < len(encoded_str) and depth != 0:
                        if encoded_str[i] == "[":
                            depth += 1
                        elif encoded_str[i] == "]":
                            depth -= 1
                        repeat_substr += encoded_str[i] if depth != 0 else ""
                        i += 1
                    decoded_str += decode(int(repeat_count), repeat_substr)
                else:
                    decoded_str += encoded_str[i]
                    i += 1
            return decoded_str * n

        return decode(1, s)
