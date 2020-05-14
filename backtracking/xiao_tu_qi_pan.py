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

#小兔的棋盘
#https://zhuanlan.zhihu.com/p/83052341
class SearchTree(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.childs = []

def find_path_on_chess_borad(N, T, i, j):
    t = SearchTree()
    t.x = i
    t.y = j
    T.childs.append(t)
    if i + 1 < N:
        find_path_on_chess_borad(N, t, i + 1, j)
    
    if j + 1 <= i:
        find_path_on_chess_borad(N, t, i, j + 1)
    return

count = 0
def traverse(T):
    global count
    print("%d,%d"%(T.x, T.y))
    if len(T.childs) == 0:
        print("-----")
        count = count + 1
        return

    for ch in T.childs:
        traverse(ch)
    return


if __name__ == '__main__':
    T = SearchTree()
    find_path_on_chess_borad(5, T, 1, 0)
    traverse(T)
    print(count)
    #quit
    print("Quit successfull");

 
