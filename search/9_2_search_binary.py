'''
 $Revision: 1.0 $
 $Author: kunzhong $
 $Date: 2020/03/16 $
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
        

if __name__ == '__main__':

    search_binary([1,2, 3, 4, 5], 6)
    #quit
    print("Quit successfull");



