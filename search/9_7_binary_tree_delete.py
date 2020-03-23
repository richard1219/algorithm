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
  

#删除一个二叉树节点
#@node_p 要删除的节点
#@node_p_parent 要删点的父节点
def delete_binary_tree(node_p_parent, node_p):
    #假如删除的是某个节点的左孩子
    if node_p_parent.left_child == node_p:
        if not node_p.right_child:
            node_p_parent.left_child = node_p.left_child
        elif not node_p.left_child:
            node_p_parent.left_child = node_p.right_child
        else:
            node_s = node_p.left_child
            node_s_parent = node_s
            while node_s.right_child: #找到最右叶子节点，也就是左子树最大节点
                node_s_parent = node_s
                node_s = node_s.right_child

            if node_s_parent != node_s: #左子树不止一个节点
                node_s_parent.right_child = node_s.left_child
                node_s.left_child = node_p.left_child
                
            node_s.right_child = node_p.right_child
            node_p_parent.left_child = node_s
    
    elif node_p_parent.right_child == node_p:
        if not node_p.right_child:
            node_p_parent.right_child = node_p.left_child
        elif not node_p.left_child:
            node_p_parent.right_child = node_p.right_child
        else:
            node_s = node_p.left_child
            node_s_parent = node_s
            while node_s.right_child:
                node_s_parent = node_s
                node_s = node_s.right_child

            if node_s_parent != node_s:
                node_s_parent.right_child = node_s.left_child
                node_s.left_child = node_p.left_child
            
            node_s.right_child = node_p.right_child
            node_p_parent.right_child = node_s
            
    else:
        print("not mached")

    return

#查找二叉排序树，返回查到的节点
#@array index start from 1
#@low start from 1

node_key_parent = None #parent of key node
def search_binary_tree(bi_tree, key):
    global node_key_parent
    if bi_tree.data == key:
        print("find key %d at %d" % (key, key))
        return bi_tree
    elif bi_tree.data > key and bi_tree.left_child != None:
        node_key_parent = bi_tree
        return search_binary_tree(bi_tree.left_child, key)
    elif bi_tree.data < key and bi_tree.right_child != None:
        node_key_parent = bi_tree
        return search_binary_tree(bi_tree.right_child, key)
    else:
        print("can not find key")
        return

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
    build_binary_tree(bi_tree, [10, 20, 30, 40, 50, 60, 70, 80], 0, 7)

    find_node = search_binary_tree(bi_tree, 10)
    if node_key_parent and find_node:
        delete_binary_tree(node_key_parent, find_node)
    #quit
    print("Quit successfull");



