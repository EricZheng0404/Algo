from typing import List
def calc_drone_min_energy(route: List[List[int]]) -> int:
    n = len(route)
    fuel = 0
    res = 0
    for i in range(1, n):
        # Positive means a gain, negative means a loss
        usage = route[i - 1][2] - route[i][2]
        fuel += usage 
        if fuel < 0:
            res = max(res, -fuel)
    print(res)
    return res

route = [ [0,   2, 10],
                  [3,   5,  0],
                  [9,  20,  6],
                  [10, 12, 15],
                  [10, 10,  8] ]

print(calc_drone_min_energy(route))