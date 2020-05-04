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

#参考：https://www.cnblogs.com/skywang12345/p/3711532.html#anchor1

def floyd():
    v_name = ['A', 'B', 'C', 'D', 'E']
    #临接矩阵
    graph = [[0, 4, 100, 2, 100], [4, 0, 4, 1, 100], [100, 4, 0, 1, 3], [2, 1, 1, 0, 7], [100, 100, 3, 7, 0]]
    
    dist = graph
    #path -- 路径。path[i][j]=k表示，"顶点i"到"顶点j"的最短路径会经过顶点k。
    path = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

    i = 0
    while i < len(v_name):
        j = 0
        while j < len(v_name):
            path[i][j] = j
            j = j + 1
        
        i = i + 1

#第1次更新时，如果"a[i][j]的距离" > "a[i][0]+a[0][j]"(a[i][0]+a[0][j]表示"i与j之间经过第1个顶点的距离")，
#则更新a[i][j]为"a[i][0]+a[0][j]"。 
#同理，第k次更新时，如果"a[i][j]的距离" > "a[i][k]+a[k][j]"，则更新a[i][j]为"a[i][k]+a[k][j]"
    k = 0
    while k < len(v_name):
        i = 0
        while i < len(v_name):
            j = 0
            while j < len(v_name):
                tmp = dist[i][k] + dist[k][j]
                if dist[i][j] > tmp:
                    dist[i][j] = tmp
                    #"i到j最短路径"对应的路径，经过k
                    path[i][j] = path[i][k]
                j = j + 1
        
            i = i + 1
        k = k + 1

#结果输出
    i = 0
    while i < len(v_name):
        j = 0
        while j < len(v_name):
            print("%c to %c: %d"%(v_name[i], v_name[j], dist[i][j]) )
            j = j + 1
    
        i = i + 1

    return



if __name__ == '__main__':

    floyd()


    #quit
    print("Quit successfull");

 
