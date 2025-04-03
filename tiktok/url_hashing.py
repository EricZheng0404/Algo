from typing import List
import string

def stringDivider(url: str, k: int) -> List[str]:
    div = []
    for i in range(0, len(url), k):
        div.append(url[i:i+k]) # Python safe if range is out of bounds
    return div

def solution(url: str, hashString: str, k: int):
    divided_url = stringDivider(url, k) 
    result = ""
    length = len(hashString)
    for seg in divided_url:
        total = 0
        for c in seg:
            if c in string.ascii_lowercase:
                total += ord(c) - ord('a')
            else:
                if c == ':':
                    total += 26
                elif c == '/':
                    total += 27
                elif c == '.':
                    total += 28
        total = total % length
        result += hashString[total] 
                    
    return result


if __name__ == "__main__":
    assert stringDivider("abcd", 3) == ["abc", "d"]
    url = "https://xyz.com"
    hashString = "pqrst"
    k = 3
    print(solution(url, hashString, 4))
   