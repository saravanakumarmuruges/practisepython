def staircase(n):
        for stairs in range(1, n):
            print(' ' * (n-1), '#' * stairs)
            n -= 1
        #print('#' * num)

staircase(5)