import collections
import heapq

"""
Mistakes:
1. I forgot to use the condition if currFreq + 1 != 0, we don't need to push 
the element back to the heap.
2. I forgot to check after the first pop and the lst is empty, we need to return
an empty string. Or, it would be error
"""
class Solution:
    def reorganizeString(self, s: str) -> str:
        # A dictionary of counter. Str-frequency
        counter = collections.Counter(s)
        # max-heap
        lst = [(-freq, char) for char, freq in counter.items()]
        heapq.heapify(lst)
        res = ""
        while lst:
            # the most frequen char and its freq
            # currFreq is a negative number
            currFreq, currChar = heapq.heappop(lst)
            # If res is still emtpy or the last char in the res is not the most
            # frequent char
            if not res or res[-1] != currChar:
                res += currChar
                # If we still have more freq is not used up for the char,
                # we put it back to the queue
                if currFreq + 1 != 0:
                    heapq.heappush(lst, (currFreq + 1, currChar))
            else: 
                # If there're no other char other than the most frequent char, 
                # we know there's not enough chars 
                if not lst:
                    return ""
                secondFreq, secondChar = heapq.heappop(lst)
                res += secondChar
                if secondFreq + 1 != 0:
                    heapq.heappush(lst, (secondFreq + 1, secondChar))
                # We also want to put currChar back
                heapq.heappush(lst, (currFreq, currChar))
        return res
    
sol = Solution()
print(sol.reorganizeString("aab"))