"""
Could use a bracket map to make the solution less verbose but I will
keep it like this for simplicity and readability
"""
class Solution:
    def isValid(self, s: str) -> bool:
        brackets: list[str] = []

        for i in s:
            if i in ["(", "[", "{"]:
                brackets.append(i)
                continue
            match i:
                case ")":
                    if brackets.pop() != "(":
                        return False
                case "]":
                    if brackets.pop() != "[":
                        return False
                case "}":
                    if brackets.pop() != "{":
                        return False
                case _:
                    continue

        if brackets:
            return False

        return True
