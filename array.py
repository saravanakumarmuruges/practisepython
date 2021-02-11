#n = num
#arr = array

def revarray(li):
    length = len(li) - 1
    result = []
    string = ''
    while length >= 0:
        string = string + ' ' + str(li[length])
        length -= 1
    return string.lstrip()

print(revarray([1,2,3,4]))