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

#解几道笔试题吧
#参考：https://zhuanlan.zhihu.com/p/79957598

#ip还原问题
#写出一个大意，解题思路写出来了，没空写出全部限制条件
#用回溯试探法，逐点，逐一列举每个点可能的位置，将子串作为下个点的原串，最多递归4层即可解出全部
#这个有点像8皇后问题，关键是那3个点要逐点点上去
def ipaddress_seperation(ipstr, level):
    ip_len = len(ipstr)
    if ip_len == 0 or level > 4:
        return
    
    if level == 1 and ip_len < 4:
        return
    if level == 2 and ip_len < 3:
        return
    if level == 3 and ip_len < 2:
        return
    if level == 4 and ip_len < 1:
        return
    if level == 4 and ip_len > 3:
        return

    if level == 4: #到第3个点了，直接打出来
        print(ipstr)
        return

    level = level + 1
    i = 1
    while i <= 3: #加一个点，这个IP字段可能1-3个字符长，这里没有对数值进行判断，取剩余串做递归
        pre = ipstr[0:i]
        sub = ipstr[i:]
        if len(sub) < 0:
            break
        
        ipaddress_seperation(sub, level)
        i = i + 1
    
    return

#组织优化
#这个好解，逐个暴力搜索即可，无需什么思路，写完不想测试了
class Team(object):
    def __init__(self):
        self.x = 0
        self.y = 0

def search_department(matrix, N, department_list):
    i = 0
    while i < N:
        j = 0
        while j < N:
            find = False
            for dep in department_list:
                for team in dep:
                    if (team.x == i and team.y + 1 == j) or team.x + 1 == i and (team.y == j): #join dep
                        t = Team()
                        t.x = i
                        t.y = j
                        dep.append(t)
                        find = True
                        break
                if find:
                    break

            if find == False: #new department
                dep = []
                t = Team()
                t.x = i
                t.y = j
                dep.append(t)
                department_list.append(dep)

            j = j + 1
        i = i + 1
    return


#金币买装备
#回溯法解决所有烦恼？
class Coin(object):
    def __init__(self):
        self.x = 0
        self.y = 0

#设置一个最大全局级别，各种组合和他进行比较，比他大的更新他
max_grade = 0

#n：总金币数
#m: 最大可带装备数
#coins, coins_index: 装备价格和级数
#buy_num，已经买的装备数量；
#current_grade,已经买的装备数量总级别
def buy_coin(n, m, coins, coins_index, buy_num, current_grade):
    global max_grade
    coin = coins[coins_index]

    i = 0
    tem_grade = 0
    while i <= n/coin.x: #注意这里的循环的意思是买这个级别的装备0个，1个...，所以每个循环是个选择，不同循环间没有叠加效应
        tmp_num = buy_num + i

        if tmp_num > m: #退出条件之一，装备满了
            if max_grade < current_grade:
                max_grade = current_grade
            break

        spend = i * coin.x
        grade = i * coin.y
        remain = n - spend

        tem_grade  = current_grade + grade

        if remain <= 0: #退出条件二，没钱了
            #compare
            if max_grade < tem_grade:
                max_grade = tem_grade
            break

        tmp_index = coins_index + 1
        if tmp_index >=len(coins): #退出条件三，没有装备可买了
            #compare
            if max_grade < tem_grade:
                max_grade = tem_grade

            i = i + 1
            continue #非常注意这个continue，意思是当前没有其它装备可买了，就最后装备里选

        buy_coin(remain, m, coins, tmp_index, tmp_num, tem_grade)

        i = i + 1

    return


if __name__ == '__main__':

    #ipaddress_seperation("88888", 1)

    n = 108
    m = 13
    coin1 = Coin()
    coin1.x = 10
    coin1.y = 10

    coin2 = Coin()
    coin2.x = 5
    coin2.y = 5

    coin3 = Coin()
    coin3.x = 2
    coin3.y = 1

    coins = []
    coins.append(coin1)
    coins.append(coin2)
    coins.append(coin3)

    buy_coin(n, m, coins, 0, 0, 0)
    print (max_grade)
    

    #quit
    print("Quit successfull");

 
