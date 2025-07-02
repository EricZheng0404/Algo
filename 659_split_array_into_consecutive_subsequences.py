from typing import List
class Solution:
    """
    Two cases for each num:
    1. Append to the end of a subsequence. This should be preferred because we want 
    to save for later.
    2. To start a new subsequence. 
    """
    def isPossible(self, nums: List[int]) -> bool:
        # To keep track of the usage of the letters
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        # To keep track of needed char so we can tag it along another sequence
        need = {} 
        for num in nums:
            # If a num is used up, we don't want to use it anymore
            if freq[num] == 0:
                continue
            # If a num can be tagged along in other subsequences
            if freq[num] > 0 and num in need and need[num] > 0:
                # Update need
                need[num] -= 1
                # Update freq
                freq[num] -= 1
                # Add the next needed num
                need[num + 1] = need.get(num + 1, 0) + 1
            # Elif we need to create a new subsequence
            elif freq.get(num, 0) > 0 \
            and freq.get(num + 1, 0) > 0 \
            and freq.get(num + 2, 0) > 0:
                freq[num] -= 1
                freq[num + 1] -= 1
                freq[num + 2] -= 1
                need[num + 3] = need.get(num + 3, 0) + 1
            # Else we can nothing about it
            else:
                return False
        return True
from collections import Counter
from collections import defaultdict
class Solution2:
    def isPossible(self, nums):
        freq = Counter(nums)
        need = defaultdict(list)

        # count the frequency of elements in nums
        for v in nums:
            if freq[v] == 0:
                continue

            if need[v]:
                # v can be appended to a previous sequence
                freq[v] -= 1
                # take any subsequence that needs v
                seq = need[v].pop()
                # append v to this subsequence
                seq.append(v)
                # the requirement of this subsequence becomes v + 1
                need[v + 1].append(seq)
            elif freq[v] > 0 and freq[v + 1] > 0 and freq[v + 2] > 0:
                # can use v as the start
                freq[v] -= 1
                freq[v + 1] -= 1
                freq[v + 2] -= 1
                # create a subsequence of length 3 [v, v + 1, v + 2]
                seq = [v, v+1, v+2]
                # increase the need for v + 3 by one
                need[v + 3].append(seq)
            else:
                return False

        # print all the subsequences that have been split out
        for v, seqs in need.items():
            for seq in seqs:
                print(v, ' '.join(map(str, seq)))

        return True
    
sol = Solution2()
print(sol.isPossible([1,2,3,3,4,5]))