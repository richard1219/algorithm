'''
 $Revision: 1.0 $
 $Author: kunzhong $
 $Date: 2020/03 $
'''

import time
import signal
import socket
import string
import struct
import re
import subprocess
import platform
import sys
import os
import math

#bubble sort
def bubble_sort(array):
    for j in range(0, len(array) - 1):
        for i in range(0, len(array) - j - 1):
            if array[i] > array[i + 1]:
                tmp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = tmp

    return

#quick sort partition
def quick_sort_partition(array, low, high):
    pivot = low
    while high > low:
        while array[high] > array[pivot] and high > low:
            high = high - 1
        tmp = array[high]
        array[high] = array[pivot]
        array[pivot] = tmp
        pivot = high
            
        while array[low] < array[pivot] and high > low:
            low = low + 1
        tmp = array[low]
        array[low] = array[pivot]
        array[pivot] = tmp
        pivot = low
    
    return pivot

def quick_sort(array, low, high):
    if high > low:
        pivot = quick_sort_partition(array, low, high)

        quick_sort(array, low, pivot - 1)
        quick_sort(array, pivot + 1, high)
  
    

if __name__ == '__main__':

    array = [50, 10, 20, 80, 70, 60, 90, 30]
    #bubble_sort(array)
    quick_sort(array, 0, len(array) - 1)
    print(array)

    #quit
    print("Quit successfull");

 
