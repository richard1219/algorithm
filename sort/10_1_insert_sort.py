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

#直接插入排序
def insert_sort(array):
    for i in range(1, len(array)):
        insert_item = array[i]
        for j in range(0, i):
            if array[j] > insert_item:
                k = i
                while k > j:
                    array[k] = array[k - 1]
                    k = k -1
                array[j] = insert_item
                break
    return


if __name__ == '__main__':

    array = [50, 10, 20, 80, 70, 60, 90, 30]
    insert_sort(array)
    print(array)

    #quit
    print("Quit successfull");



