from typing import List

views = [2, 3, 4, 5, 6]
likes = [4, 6, 5, 7, 3]

def solution(views: List[int], likes: List[int]):
    # Write your code her
    new_likes = sorted(likes) 
    print(new_likes)

def check():
    pass

solution(views, likes)