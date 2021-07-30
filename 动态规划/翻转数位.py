# -*- coding:utf-8 -*-
# @Time    : 2021/7/30 9:16
# @Author  : zengln
# @File    : 翻转数位.py

# 给定一个32位整数 num，你可以将一个数位从0变为1。请编写一个程序，找出你能够获得的最长的一串1的长度。
#
#  示例 1：
#
#  输入: num = 1775(110111011112)
# 输出: 8
#
#
#  示例 2：
#
#  输入: num = 7(01112)
# 输出: 4
#
#  Related Topics 位运算 动态规划

class Solution:
    def reverseBits(self, num: int) -> int:
        """
        当前位置为0，所以机会要在这里用掉，前面只能计算前面连续1的个数，而不是最长1的个数
        当前位置N最长获取1的个数 = 前面连续1的个数 + 1

        当前位置为1
        当前位置N最长获取1的个数 = 位置N-1最长获取1的个数 + 1
        """
        # 当前连续1的个数
        cur = 0
        # 当前最长获取1的个数
        index = 0
        # 记录的最长个数
        result = 0
        for i in range(32):
            if num & (1 << i):
                cur += 1
                index += 1
            else:
                index = cur+1
                cur = 0
            result = max(result, index)
        return result



