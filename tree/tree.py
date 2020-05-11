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



class Tree(object):
    def __int__(self):
        self.data = 0
        self.lchild = None
        self.rchild = None
        
#非递归方式，先序遍历了一颗二叉树，开胃菜
def traverse_no_recursive(T):
    stack = [] #用个栈保存未访问的右孩子，完美
    while T != None:
        print(T.data) #access
        if T.rchild != None:
            stack.append(T.rchild)
        T = T.lchild
        if T == None:
            if len(stack) != 0:
                child = stack.pop()
                T = child
            else:
                print("done")
                return
           
    return

#递归方式先序遍历树
def traverse_front(T):
    if T != None:
        print(T.data)
        if T.lchild != None:
            traverse_front(T.lchild)
        
        if T.rchild != None:
            traverse_front(T.rchild)
    return

def traverse_test():
    t5 = Tree()
    t5.data = 5
    t5.lchild = None
    t5.rchild = None

    t4 = Tree()
    t4.data = 4
    t4.lchild = None
    t4.rchild = None

    t3 = Tree()
    t3.data = 3
    t3.lchild = None
    t3.rchild = None

    t2 = Tree()
    t2.data = 2
    t2.lchild = t4
    t2.rchild = t5

    t1 = Tree()
    t1.data = 1
    t1.lchild = t2
    t1.rchild = t3

    traverse_no_recursive(t1)
    print("recursive:")
    traverse_front(t1)



if __name__ == '__main__':

    traverse_test()

    #quit
    print("Quit successfull");

 
