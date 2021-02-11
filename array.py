#n = num
#arr = array

def revarray(li):
    length = len(li) - 1
    result = []
    string = ' '
    while length >= 0:
        result.append(li[length])
        length -= 1
    return string.join(str(result))

print(revarray([1,2,3,4]))