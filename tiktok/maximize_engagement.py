from typing import List

views = [2, 3, 4, 5, 6]
likes = [4, 6, 5, 7, 3]
# likes excceeds views

def solution(views: List[int], likes: List[int]):
    # Write your code her
    new_likes = sorted(likes) 
    result = 0
    for num in views:
        if num < new_likes[result]:
            result += 1
    return result

def check():
    pass

print(solution(views, likes))