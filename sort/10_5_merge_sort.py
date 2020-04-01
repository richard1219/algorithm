'''
 $Revision: 1.0 $
 $Author: kunzhong $
 $Date: 2020/04 $
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

#merge sort
#在同一队列中进行移动，避免开辟新空间，类似插入排序
def merge(array, i, m, n):
    x = i
    y = m + 1
    while x <= m and y <= n:
        if array[x] <= array[y]:
            x = x + 1
        else:
            tmp = array[y]
            k = y
            while k > x:
                array[k] = array[k - 1]
                k = k - 1
            array[x] = tmp
            x = x + 1
            y = y + 1
            m = m + 1

    return

#这种实现方式有概念上的意义但无实际意义，比较和移动次数并不少，递归还耗用栈空间
#但这是一种很好的递归调用演示
def merge_sort(array, i, n):
    if i == n: #递归退出条件
        return
    
    m = int((i + n)/2) #分两部分递归
    merge_sort(array, i, m)  
    merge_sort(array, m + 1, n)
    merge(array, i, m, n) #合并两部分
    return


if __name__ == '__main__':

    array = [50, 10]
    merge_sort(array, 0, len(array) - 1)
    print(array)

    #quit
    print("Quit successfull");

 
