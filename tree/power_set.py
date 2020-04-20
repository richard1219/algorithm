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


#search tree
class SearchTree(object):
    def __init__(self):
        self.data = None
        self.parent = None
        self.childs = []


#build the search tree
#@theset the set in array
#@thetree the search tree
def power_set_build_search_tree(theset, thetree):
    if thetree.data == None:
        i = 0
    else:
        i = thetree.data + 1

    while i < len(theset):
        t = SearchTree()
        t.data = i
        t.parent = thetree
        thetree.childs.append(t)
        power_set_build_search_tree(theset, t)
        i = i + 1

    return

def traverse(theset, thetree):
#    if thetree.data != None:
#        print(theset[thetree.data])
    
    if len(thetree.childs) == 0:
        tmp = thetree
        while tmp.parent != None:
            print(theset[tmp.data])
            tmp = tmp.parent
        print(";")
    
    for t in thetree.childs:
        traverse(theset, t)

    return


if __name__ == '__main__':

    theset = [1, 2, 3]
    tree = SearchTree()
    power_set_build_search_tree(theset, tree)
    traverse(theset, tree)

    #quit
    print("Quit successfull");

 
