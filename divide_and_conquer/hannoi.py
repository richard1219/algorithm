'''
 $Revision: 1.0 $
 $Author: kunzhong $
 $Date: 2020/05 $
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
import zlib
import base64


#好绕啊，果真是源于佛和缠的问题，问题简单的要命，解法也简单的要命，但一时我也没有悟透其真意，再来！
def hannoi(n, A, B, C):
    if n == 1:
        a = A.pop()
        C.append(a)
    else:
        hannoi(n - 1, A, C, B)
        a = A.pop()
        C.append(a)
        hannoi(n - 1, B, A, C)

    return


if __name__ == '__main__':
    A = []
    B = []
    C = []
    n = 16
    for i in range(0, n):
        A.append(n - i)

    hannoi(n, A, B, C)

    #quit
    print("Quit successfull")

 
