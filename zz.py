from typing import List
def f(weights: List[int], x: int) -> int:
    days = 0
    # load as much as possible
    i = 0
    while i < len(weights):
        cap = x
        while i < len(weights):
            if cap < weights[i]:
                break
            else:
                cap -= weights[i]
                i += 1
        days += 1
    return days

weights = [1,2,3,1,1]
days = 4
print(f(weights, 3))