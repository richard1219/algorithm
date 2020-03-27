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

#simple selection sort
def simple_selection_sort(array):
    for j in range(0, len(array) - 1):
        min = array[j]
        min_index = j
        for i in range(j + 1, len(array)):
            if min > array[i]:
                min = array[i]
                min_index = i
        
        if min_index != j:
            tmp = array[j]
            array[j] = array[min_index]
            array[min_index] = tmp

    return


if __name__ == '__main__':

    array = [50, 10, 20, 80, 70, 60, 90, 30]
    simple_selection_sort(array)
    print(array)

    #quit
    print("Quit successfull");

 
