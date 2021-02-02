#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    sum=0
    for i in ar :
        sum = sum+i
    return sum

print(simpleArraySum([1,2,3,4]))