class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] # A list of [char, count]
        for char in s:
            if stack and stack[-1][0] == char:
                if stack[-1][1] == k - 1:
                    stack.pop()
                else:
                    stack[-1][1] += 1
            else:
                stack.append([char, 1])
        return "".join([char * count for char, count in stack])