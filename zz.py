from typing import List

def get_different_number(arr: List[int]) -> int:
    n = len(arr)
    i = 0
    while i < n:
        while i < n and arr[i] != arr[arr[i]]:
            # arr[arr[i]], arr[i] = arr[i], arr[arr[i]]
            arr[i], arr[arr[i]] = arr[arr[i]], arr[i]
        i += 1
    for i in range(n):
        if i != arr[i]:
            return i
    return n

print(get_different_number([0]))