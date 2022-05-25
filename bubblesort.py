#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    count = 0

    n = len(a)
    for i in range (n) :
        for j in range (n-1):
            if(a[j]>a[j+1]):            
                a[j] = a[j+1]
                a[j+1] = a[j]
                count +=1
                
    print("The array is sorted in "+str(count)+" swaps.")
    print("The first element: " + str(a[0]) )
    print("The last element: " + str(a[-1]))
    
                
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

countSwaps(a)
