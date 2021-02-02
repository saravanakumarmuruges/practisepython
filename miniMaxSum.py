def miniMaxSum(arr):
    min = 0
    max = 0
    arr.sort()
    print(arr)
    for i in range(0, len(arr)-1):
        min = min + arr[i]

    arr.sort(reverse=True)
    for i in range(0, len(arr)-1):
        max = max + arr[i]
    return min, max

print(miniMaxSum([1,2,3,4,5]))