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


class Point(object):
    def __init__(self):
        self.x = 0
        self.y = 0

#search tree
class SearchTree(object):
    def __init__(self):
        self.data = []
        self.childs = []


#build the search tree
#@num number of queen
#@thetree search tree
#@j  j row index
def build_search_tree(num, thetree, j):
    
    for i in range(0, num):
        meet = False
        for p in thetree.data:
            if i == p.x or j == p.y:
                meet = True
                break
    
            n = 0
            while n < num:  #mach in y=kx +n
                tmp = n + (p.y - p.x)
                if tmp == j and n == i:
                    meet = True
                    break
                
                if tmp >= num:
                    break
                n = n + 1

            if meet:
                break

            n = 0
            while n < num: #mach in y= -kx + n
                tmp = p.y + p.x - n
                if tmp == j and n == i:
                    meet = True
                    break

                if tmp <= 0:
                    break
                n = n + 1
            
            if meet:
                break
        
        if meet:
            continue
            
        tree = SearchTree()
        for p in thetree.data:
            tree.data.append(p)
        p = Point()
        p.x = i
        p.y = j
        tree.data.append(p)
        thetree.childs.append(tree)
        if len(tree.data) == num:
            out = ""
            for p in tree.data:
                out = out + "(" + str(p.x) + "," + str(p.y) + ")"
            print(out)

        if j + 1 < num:
            build_search_tree(num, tree, j + 1)

    return



if __name__ == '__main__':

    tree = SearchTree()
    build_search_tree(8, tree, 0)


    #quit
    print("Quit successfull");

 
