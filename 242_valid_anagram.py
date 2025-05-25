from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths are different, they can't be anagrams
        if len(s) != len(t):
            return False
            
        # Use dictionary to count characters
        char_count = {}
        
        # Count characters in first string
        for c in s:
            char_count[c] = char_count.get(c, 0) + 1
            
        # Decrement counts for second string
        for c in t:
            if c not in char_count:
                return False
            char_count[c] -= 1
            if char_count[c] == 0:
                del char_count[c]
                
        # If dictionary is empty, all characters matched
        return len(char_count) == 0