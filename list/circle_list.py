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

#grade: *****
#判断链表中是否有环 ----- 有关单链表中环的问题
#https://www.cnblogs.com/yorkyang/p/10876604.html
'''
首先，关于单链表中的环，一般涉及到一下问题：
1.给一个单链表，判断其中是否有环的存在；
2.如果存在环，找出环的入口点；
3.如果存在环，求出环上节点的个数；
4.如果存在环，求出链表的长度；
5.如果存在环，求出环上距离任意一个节点最远的点（对面节点）；
6.（扩展）如何判断两个无环链表是否相交；
7.（扩展）如果相交，求出第一个相交的节点；
'''

class List(object):
    def __init__(self):
        self.data = None
        self.next = None

#链表是否有环
#设计2个指针，一个比另一个快2倍，他们如果有环，他们必定相遇
def find_list_circle(theList):
    slow = theList
    fast = theList
    while slow != None and fast != None:
        slow = slow.next
        if fast.next != None:
            fast = fast.next.next

        if slow == fast:
            return 1
    
    return 0

#链表如果有环，输出环入口
#环的入口位置，距离链表初始位置和距离slow的位置是相等的，这需要数学证明，证明过程还没搞懂；
def find_list_circle_and_entrance(theList):
    slow = theList
    fast = theList
    while slow != None and fast != None:
        slow = slow.next
        if fast.next != None:
            fast = fast.next.next

        if slow == fast:
            break
    
    if fast == None:
        return None

    fast = theList
    while fast != slow:
        fast = fast.next
        slow = slow.next

    return fast
    
#如果有环，环上节点个数
def find_list_circle_and_circle_number(theList):
    slow = theList
    fast = theList
    while slow != None and fast != None:
        slow = slow.next
        if fast.next != None:
            fast = fast.next.next

        if slow == fast:
            break

    if fast == None:
        return 0

    count = 1
    cur = slow.next
    while cur != slow:
        count = count + 1

    return count

#6.（扩展）如何判断两个无环链表是否相交；
#7.（扩展）如果相交，求出第一个相交的节点；
#将其中一个链表头尾相接为一个环，问题转换为1,2


if __name__ == '__main__':

  
    #quit
    print("Quit successfull")

 
