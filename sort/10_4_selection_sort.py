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

#simple selection sort
def simple_selection_sort(array):
    for j in range(0, len(array) - 1):
        min = array[j]
        min_index = j
        for i in range(j + 1, len(array)):
            if min > array[i]:
                min = array[i]
                min_index = i
        
        if min_index != j:
            tmp = array[j]
            array[j] = array[min_index]
            array[min_index] = tmp

    return

#堆排序是一种树型选择排序，是对常规树型选择排序的改进
#堆的翻译也很传神，完全二叉树，非终端节点不大于或小于左右孩子节点，形象的组成了一堆
#heap adjust
#@array starts from 1
#@s 开始构造的序号
#@m 结束构造的序号
#构造大顶堆，从堆顶开始进行调整
def heap_adjust(array, s, m):
    peak = array[s]
    j = 2*s
    while j <= m:
        if j < m and array[j] < array[j + 1]:
            j = j + 1
        if peak >= array[j]:
            break
        array[s] = array[j]
        array[j] = peak
        s = j
        j = s * 2
        
    return

#技巧性很强很巧妙有点tricky的排序，很好的利用了完全二叉树根与叶子节点的位置关系
#堆的概念应该是基于完全二叉树概念提出，并且应该专门是服务于排序的
#堆的概念一般定义为：Ki <= K2i; Ki <= K2i+1, i = 1... n/2; （或大于）
#可以另外更形象的表述为：堆是一种完全二叉树，该二叉树及其任意子树根节点小于等于叶子节点 （或大于）
def heap_sort(array):
    #构造大顶堆，从最小子树开始 最后非终端节点开始
    i = int((len(array) - 1)/2)
    while i > 0:
        heap_adjust(array, i, len(array) - 1)
        i = i - 1

    i = 1
    while i < len(array) -1:
        #把大顶堆堆顶换到堆尾
        tmp = array[len(array) - i]
        array[len(array) - i] = array[1]
        array[1] = tmp
        #把剩余未排序的从堆顶排到堆尾
        heap_adjust(array, 1, len(array) - i -1)
        i = i + 1



if __name__ == '__main__':

    array = [0, 49, 38, 65, 98, 76, 13, 27, 49]
    heap_sort(array)
    print(array)

    #quit
    print("Quit successfull");

 
