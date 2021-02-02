def diagonalDifference(arr):
    left=0 #O(1)
    right=0 #O(1)
    max_row=len(arr) - 1 #O(1)
    for i in range(0, len(arr)): #O(n)
        left = left + arr[i][i]
    for i in range(0, len(arr)): #O(n)
        right = right + arr[i][max_row]
        max_row = max_row - 1
    return abs((right -left)) #O(1)

sample = list([[6, 6, 7, -10, 9, -3, 8, 9, -1,],
 [9, 7, -10, 6, 4, 1, 6, 1, 1,],
 [-1, -2, 4, -6, 1, -4, -6, 3, 9],
 [-8, 7, 6, -1, -6, -6, 6, -7, 2],
 [-10, -4, 9, 1, -7, 8, -5, 3, -5],
 [-8, -3, -4, 2, -3, 7, -5, 1, -5],
 [-2, -7, -4, 8, 3, -1, 8, 2, 3],
 [-3, 4, 6, -7, -7, -8, -3, 9, -6],
 [-2, 0, 5, 4, 4, 4, -3, 3, 0]])

out=diagonalDifference(sample)
print(out)