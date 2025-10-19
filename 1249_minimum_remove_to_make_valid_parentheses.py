class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i, char in enumerate(s):
            if char not in ["(", ")"]:
                continue
            if char == "(":
                stack.append((char, i))
            else:
                if stack and stack[-1][0] == "(":
                    stack.pop()
                else:
                    stack.append((char, i))
        stack = set(stack) # This is also O(n)
        res = []
        for i, char in enumerate(s):
            if (char, i) in stack:
                continue
            res.append(char)
        return "".join(res)