
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

count = 0
while n:
    n &= n << 1
    print(n)
    count += 1

print(count)