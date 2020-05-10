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

#二分查找法
#@array 要查找的数组
#@key 要查找的关键字
def search_binary(array, key):
    i_start = 0
    i_end = len(array) - 1
    counter = 0

    while i_end >= i_start :
        i_mid = int((i_start + i_end)/2)
        counter = counter + 1
        if (array[i_mid] == key) :
            print("find key=%d at %d, compare times: %d" % ( key, i_mid, counter))
            return
        elif (array[i_mid] > key) :
            i_end = i_mid - 1
        else :
            i_start = i_mid + 1
    
    print("no mached key, compare times: %d" % counter)
    return

#用递归法重写一遍
#start: 查找起始序号
#end: 结束序号
def search_binary2(array, start, end, key):
    mid = int((start + end) / 2)

    if (start > end): #要注意这个递归退出条件，否则死循环错误
        print("not found")
    elif array[mid] == key:
        print("find key at %d" % mid)
    elif array[mid] > key:
        search_binary2(array, start, mid - 1, key)
    elif array[mid] < key:
        search_binary2(array, mid + 1, end, key)

    return

if __name__ == '__main__':

    arr = [10, 20, 30, 40, 50, 70]
    search_binary(arr, 26)

    search_binary2(arr, 0, len(arr) - 1, 6)
    #quit
    print("Quit successfull");



