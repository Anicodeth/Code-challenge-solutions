#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    for i in range(1,n):
        for j in range(i,0,-1):
            if(arr[j-1]>arr[j]):
                temp=arr[j-1]
                arr[j-1]=arr[j]
                arr[j]=temp
        for i in arr:
            print(i,end=' ')
            
        print()
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
