class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # use stacks
        s_stack = []
        t_stack = []

        for i in s:
            if i == "#":
                if s_stack:
                    s_stack.pop()
                continue
            s_stack.append(i)

        for i in t:
            if i == "#":
                if t_stack:
                    t_stack.pop()
                continue
            t_stack.append(i)

        return "".join(s_stack) == "".join(t_stack)
