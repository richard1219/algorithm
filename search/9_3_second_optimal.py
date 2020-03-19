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

class BinaryTree(object):
    def __init__(self):
        self.data = None
        self.left_child = None
        self.right_child = None
  

#构建次优查找树
#@array index start from 1
#@low start from 1
def second_optimal(bi_tree, array, sw, low, high):
    dw = sw[high] + sw[low - 1]
    min_p = abs(dw - sw[low] - sw[low -1])
    target_i = low
    j = low

    while j < high:
        p = abs(dw - sw[j] - sw[j -1])
        if p < min_p:
            target_i = j
            min_p = p 
        j = j + 1

    #bi_tree = BinaryTree() #不能传引用，所以对象在函数外建立
    bi_tree.data = array[target_i]

    if target_i == low:
        bi_tree.left_child = None
    else:
        bi_tree.left_child = BinaryTree()
        second_optimal(bi_tree.left_child, array, sw, low, target_i - 1)

    if target_i == high:
        bi_tree.right_child = None
    else:
        bi_tree.right_child = BinaryTree()
        second_optimal(bi_tree.right_child, array, sw, target_i + 1, high)

    return
        

if __name__ == '__main__':

    array = [0, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    array_power = [0, 1, 1, 2, 5, 3, 4, 4, 3, 5]
    sw = [0]
    for i in range(1, len(array_power)):
        sum = array_power[i] + sw[i - 1]
        sw.append(sum)
    
    bi_tree = BinaryTree()
    second_optimal(bi_tree, array, sw, 1, len(array) - 1)
    #quit
    print("Quit successfull");



