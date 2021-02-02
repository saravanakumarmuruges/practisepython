def plus_minus(arr):
    positive = 0
    neg = 0
    zero = 0
    n = len(arr)
    for i in arr:
        if i > 0:
            positive = positive + 1
        elif i < 0:
            neg = neg + 1
        else:
            zero = zero + 1
    pos_ratio = round ((positive/n), 6)
    neg_ratio = round ((neg/n), 6)
    zero_ratio = round ((zero/n), 6)
    print("{:.6f}".format(pos_ratio))
    print("{:.6f}".format(neg_ratio))
    print("{:.6f}".format(zero_ratio))

plus_minus([-4, 3, -9, 0, 4, 1])
