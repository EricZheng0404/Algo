from typing import List
def knapsack(W: int, wt: List[int], val: List[int]) -> int:
    N = len(wt)
    # base case has been initialized
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for w in range(1, W + 1):
            if w - wt[i-1] < 0:
                # in this case, we can only choose not to put it in the backpack
                dp[i][w] = dp[i - 1][w]
            else:
                # choose the best option between putting it in the backpack or not
                dp[i][w] = max(
                    dp[i - 1][w - wt[i-1]] + val[i-1], 
                    dp[i - 1][w]
                )
    print(dp)
    return dp[N][W]

print(knapsack(4, [2, 1, 3], [4, 2, 4]))