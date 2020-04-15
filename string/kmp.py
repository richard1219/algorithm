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

#kmp next
#@next_array start from 1
def next(pattern, next_array):
    next_array.append(0)
    next_array.append(0)
    next_array.append(1)
    i = 2
    j = 1

    while i < len(pattern): 
        if j == 0 or pattern[i - 1] == pattern[j - 1]:
            i = i + 1
            j = j + 1
            next_array.append(j)
        else:
            j = next_array[j]

    return

#better next
def next2(pattern, next_array):
    next_array.append(0)
    next_array.append(0)
    next_array.append(1)
    i = 2
    j = 1

    while i < len(pattern): 
        if j == 0 or pattern[i - 1] == pattern[j - 1]:
            i = i + 1
            j = j + 1
            if pattern[i - 1] != pattern[j - 1]:
                next_array.append(j)
            else:
                next_array.append(next_array[j])
        else:
            j = next_array[j]

    return

#kmp
def kmp(src_string, pattern):
    i = 0
    j = 0
    next_array = []
    next(pattern, next_array)

    while i < len(src_string):
        if src_string[i] == pattern[j]:
            i = i + 1
            j = j + 1
            if j >= len(pattern):
                print("find pattern %d" % (i - 1))
                return
        else:
            j = next_array[j]
            if j == 0:
                i = i + 1

        
    print("no matched string")
    return

if __name__ == '__main__':

    pattern = "aaaaaaab"
    next_array = []
    next2(pattern, next_array)

    pattern = "aaacd"
    src_string = "cadaaaacdks"
    kmp(src_string, pattern)

    #quit
    print("Quit successfull");

 
