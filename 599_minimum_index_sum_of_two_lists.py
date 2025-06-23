class Solution:
    """
    Question 1: How to constantly look up min index and also update the result array.
    Answer: We could just discard the old list

    Steps:
    1. Build a hashmap with word: i using list1.
    2. Set up a res array list and minIndexSum.
    3. Iterate through list2
        4. If there's a match using hashmap, we first compare it with minIndexSum.
            if there's a min, we update res array.
            Else, we append the element in the res.
    """

from typing import List

def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
    lookup = {word: i for i, word in enumerate(list1)}
    res = []
    minIndexSum = float("inf")
    for i, word in enumerate(list2):
        if word in lookup: 
            sumIndex = i + lookup[word]
            if sumIndex < minIndexSum:
                res = [word]
                minIndexSum = sumIndex # We need to update the minIndex
            elif sumIndex == minIndexSum: # This is a elif. Or we could update the minIndexSum and the word will be appended twice.
                res.append(word)
    return res