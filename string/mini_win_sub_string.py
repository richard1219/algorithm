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

#76. 最小覆盖子串
#https://leetcode-cn.com/problems/minimum-window-substring/
'''
给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。

示例：

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
说明：

如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-window-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

#这是个滑动窗口问题：在滑动窗口类型的问题中都会有两个指针。一个用于延伸现有窗口的 rightright 指针，和一个用于收缩窗口的 leftleft 指针。在任意时刻，只有一个指针运动，而另一个保持静止。
#可以优化到 O(∣S∣+∣T∣)

#性能不好的算法 O(m*n)
#有可能做到kmp算法的复杂度吗
def mini_sub_string(str, sub_str):
    flag = {}
    start = 0
    i = 0
    while i < len(str):
        for j in range(len(sub_str)): #这段比较可以优化，对子串进行排序和二分查找，复杂度减低到m*logn
            if (str[i] == sub_str[j]):
                flag[sub_str[j]] = 1
            else:
                continue
            
            if len(flag) == 1:
                start = i
            
            find = True
            for k in range(len(sub_str)):
                if flag.has_key(sub_str[k]) == False:
                    find = False
                    break

            if find:
                print("sub start %d, len=%d" %(start, i))
                i = start + 1 #find next
                flag = {}
                start = 0
                continue
        
        i = i + 1
    return

if __name__ == '__main__':

    mini_sub_string("ADOBECODEBANC", "ABC")
    #quit
    print("Quit successfull");

 
