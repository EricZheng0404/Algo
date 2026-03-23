from collections import defaultdict
def solution(matrix):
    n = len(matrix)
    # Get the (row, col) for cells in Y
    y_cells = set([(n // 2, n // 2)])
    for i in range(n // 2):
        y_cells.add((0 + i, 0 + i))
        y_cells.add((0 + i, n - 1 - i))
        y_cells.add((n - 1 - i, n // 2))
    print("y_cells: ", y_cells)
    # Get the current number of 0's, 1's, and 2's in Y and other
    # Every item is [number, frequency]
    y = [[0, 0], [1, 0], [2, 0]] 
    other = [[0, 0], [1, 0], [2, 0]]
    for row in range(n):
        for col in range(n):
            num = matrix[row][col]
            if (row, col) in y_cells:
                y[num][1] += 1
            else:
                other[num][1] += 1
    # Get the final number for Y and other
    # Sort by the frequency of the numbers
    # The largest frequency is the last item
    y.sort(key=lambda x:x[1])
    other.sort(key=lambda x:x[1])
    print(y)
    print(other)
    # If the numbers of greateset frequency are different in Y and other
    if y[-1][0] != other[-1][0]:
        return y[0][1] + y[1][1] + other[0][1] + other[1][1]
    else:
        # If Y takes the number of greateset frequency
        change1 = y[0][1] + y[1][1] + other[0][1] + other[2][1]
        # Other takes the number of greatest frequency
        change2 = y[0][1] + y[2][1] + other[0][1] + other[1][1]
    return min(change1, change2)
    
matrix1 = [
    [1, 0, 2],
    [1, 2, 0], 
    [0, 2, 0],
]

matrix2 = [
    [2, 0, 0, 0, 2],
    [1, 2, 1, 2, 0],
    [0, 1, 2, 1, 0],
    [0, 0, 2, 1, 1],
    [1, 1, 2, 1, 1],
]

matrix3 = [
    [1, 0, 2, 2, 1],
    [2, 1, 2, 1, 2],
    [2, 2, 1, 1, 1],
    [1, 1, 2, 1, 1],
    [1, 1, 2, 1, 1],
]
# assert solution(matrix1) == 2
# assert solution(matrix2) == 8
assert solution(matrix3) == 13