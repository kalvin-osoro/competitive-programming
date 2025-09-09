#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    #iterate through the list containing 100 integer values, 
    #Each time a value occurs on the array, increment by1 in that index from 0 through 99
    nums = [0] * 100
    for i in range(len(arr)):
        val = arr[i]
        
        if (0<=val<=100):
            nums[val] +=1
    return nums
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
