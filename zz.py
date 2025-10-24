def flatten(s):
    res = []
    char = None
    count = 0
    for c in s:
        if char is None or char != c:
            if char != None:
                res.append(char)
                res.append(count)
            char = c
            count = 1
        elif char == c:
            count += 1
    res.append(char)
    res.append(str(count))
    return "".join(res)

def flatten2(s):
    res = []
    char = s[0]
    count = 1
    for i in range(1, len(s)):
        c = s[i]
        if c != char:
            res.append(f"{char}{count}")
            char = c
            count = 1
        else:
            count += 1
    res.append(f"{char}{count}")
    return "".join(res)

res = print(flatten2("aaabbc"))
"""
Input: "aaabbc"
Output: "a3b2c1"

res = a, 3, b, 2
char = c
count = 1
"""