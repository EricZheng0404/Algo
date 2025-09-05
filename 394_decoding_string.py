class Solution:
    def decodeString(self, s: str) -> str:
        # "3[a]2[bc]"
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            # To get the to-be-decoded string
            else:
                codedList = []
                while stack and stack[-1] != "[":
                    codedList.append(stack.pop())
                codedList.reverse()
                # To remove the extra "["
                if stack:
                    stack.pop()
                # To get the times of repetition
                times = 0
                base = 1
                while stack and stack[-1].isdigit():
                    times += base * int(stack.pop())
                    base *= 10
                for _ in range(times):
                    stack.extend(codedList)
                print(stack)
        return "".join(stack)
            

