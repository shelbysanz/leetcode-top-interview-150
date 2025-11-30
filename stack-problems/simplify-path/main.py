class Solution:
    def simplifyPath(self, path: str) -> str:
        arr: list[str] = path.split("/")
        path_stack: list[str] = []
        for i in arr:
            if not i or i == ".":
                continue
            if i == "..":
                if path_stack:
                    _ = path_stack.pop()
            else:
                path_stack.append(i)
        return "/" + "/".join(path_stack)
