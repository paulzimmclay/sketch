#!/bin/python3

import os
import sys
import functools

#
# Complete the simpleArraySum function below.
#

def simpleArraySum(ar):
    list_sum = functools.reduce((lambda x, y: x + y), ar)
    return list_sum

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     ar_count = int(input())

#     ar = list(map(int, input().rstrip().split()))

#     result = simpleArraySum(ar)

#     fptr.write(str(result) + '\n')

#     fptr.close()

print(simpleArraySum([1, 2, 3]))