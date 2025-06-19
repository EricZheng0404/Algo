import heapq
def minInterval(A, queries):
    A = sorted(A)[::-1]
    print(f"A: {A}")
    h = []
    res = {}
    for q in sorted(queries):
        while A and A[-1][0] <= q:
            i, j = A.pop()
            if j >= q:
                heapq.heappush(h, [j - i + 1, j])
        while h and h[0][1] < q:
            heapq.heappop(h)
        res[q] = h[0][0] if h else -1
    return [res[q] for q in queries]

A = [[1,4],[2,4],[3,6],[4,4]]
queries = [2,3,4,5]
print(minInterval(A, queries))