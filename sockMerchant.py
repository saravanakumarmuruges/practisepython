def sockMerchant(n, ar):
    pairs = 0
    unique_color = [] #O(1)
    for color in ar: #O(n)
        if color in unique_color:
            pass
        else:
            unique_color.append(color)
    for color in unique_color:
        if ((ar.count(color) >1) and (ar.count(color) % 2 == 0)) :
            pairs = pairs + (ar.count(color) / 2)
        elif ((ar.count(color) >1) and (ar.count(color) % 2 != 0)) :
            pairs = pairs + ((ar.count(color)-1)/2)
    return int(pairs)


print(sockMerchant(9,[10, 20, 20, 10, 10, 30, 50, 10, 20]))