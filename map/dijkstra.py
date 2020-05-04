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

#参考：https://houbb.github.io/2020/01/23/data-struct-learn-03-graph-dijkstra
#算法很容易，松弛算法为何奏效需要证明
def dijkstra():
    v_name = ['A', 'B', 'C', 'D', 'E']
    #临接矩阵
    graph = [[0, 4, 100, 2, 100], [4, 0, 4, 1, 100], [100, 4, 0, 1, 3], [2, 1, 1, 0, 7], [100, 100, 3, 7, 0]]
    
    #第一个点作为起点，自己加入已确定点
    v = [0, 0, 0, 0, 0]
    v[0] = 1

    #第一个点作为起点，初始化它到各点距离
    dis = [0, 4, 100, 2, 100]
    dis[0] = 0

    i = 0
    while i < len(v) - 1:
        k = 0

        #dis中 选个最小的
        j = 0
        while j < len(v):
            if not v[j] and (dis[j]<dis[k] or k == 0):
                k = j
            j = j + 1
        
        v[k] = 1
        print("find %c, dis %d" % (v_name[k], dis[k]))

        #松弛
        j = 0
        while j < len(v):
            if not v[j] and dis[k] + graph[k][j] < dis[j]:
                dis[j] =  dis[k] + graph[k][j]
            j = j + 1

        i = i + 1

    return



if __name__ == '__main__':

    dijkstra()


    #quit
    print("Quit successfull");

 
