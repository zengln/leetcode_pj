# -*- coding:utf-8 -*-
# @Time : 2021/7/18 16:02 
# @Author : zengln
# @File : 杨辉三角.py 
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
#
#
#
#  在杨辉三角中，每个数是它左上方和右上方的数的和。
#
#  示例:
#
#  输入: 5
# 输出:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
#  Related Topics 数组 动态规划



class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(1, numRows+1):
            temp = list()
            if i == 1:
                temp.append(1)
            else:
                last = result[-1]
                temp.append(1)
                for i in range(1, len(last)):
                    temp.append(last[i]+last[i-1])
                temp.append(1)

            result.append(temp)
        return result


