def compareTriplets(a, b):
    i=0
    alice = 0
    bob = 0
    while(i < len(a)):
        if (a[i] > b[i]):
            alice = alice + 1
        elif (a[i] < b[i]):
            bob = bob + 1
        i=i+1

    return alice,bob

print(compareTriplets([1,2,3,4,5], [6,7,8,9,10]))
print(compareTriplets([10,9,8,7,6], [5,4,3,2,1]))
print(compareTriplets([1,2,3,4,5], [1,2,3,4,5]))