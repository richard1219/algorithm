'''
 $Revision: 1.0 $
 $Author: kunzhong $
 $Date: 2020/03 $
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

#二叉树定义
class BinaryTree(object):
    def __init__(self):
        self.data = None
        self.left_child = None
        self.right_child = None
  

#查找二叉排序树
#@array index start from 1
#@low start from 1
def search_binary_tree(bi_tree, key):
    if bi_tree.data == key:
        print("find key %d at %d" % (key, key))
        return 
    elif bi_tree.data > key and bi_tree.left_child != None:
        return search_binary_tree(bi_tree.left_child, key)
    elif bi_tree.data < key and bi_tree.right_child != None:
        return search_binary_tree(bi_tree.right_child, key)
    else:
        print("can not find key")

    return

#递归法构建一颗静态二叉排序树
#@array 有序数列
def build_binary_tree(bi_tree, array, low, high):
    i_mid = int((low + high)/2)
    bi_tree.data = array[i_mid]

    if low == i_mid:
        bi_tree.left_child = None
    else:
        bi_tree.left_child = BinaryTree()
        build_binary_tree(bi_tree.left_child, array, low, i_mid - 1)

    if high == i_mid:
        bi_tree.right_child = None
    else:
        bi_tree.right_child = BinaryTree()
        build_binary_tree(bi_tree.right_child, array, i_mid + 1, high)

    return


if __name__ == '__main__':

    #构造一颗二叉排序树
    bi_tree = BinaryTree()
    build_binary_tree(bi_tree, [1, 2, 3, 4, 5, 6, 7, 8], 0, 7)

    search_binary_tree(bi_tree, 5)
    #quit
    print("Quit successfull");



