# -*- coding:utf-8 -*-
# @Time : 2021/7/19 20:37 
# @Author : zengln
# @File : 杨辉三角II.py 
# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
#
#
#
#  在杨辉三角中，每个数是它左上方和右上方的数的和。
#
#  示例:
#
#  输入: 3
# 输出: [1,3,3,1]
#
#
#  进阶：
#
#  你可以优化你的算法到 O(k) 空间复杂度吗？
#  Related Topics 数组 动态规划

class Solution:
    #[1,1]
    #[1,2,1]
    #[1,3,3,1]
    def getRow(self, rowIndex: int) -> List[int]:
        last = list()
        for i in range(1, rowIndex+2):
            temp = list()
            if i == 1:
                temp.append(1)
            else:
                temp.append(1)
                for index in range(1, i-1):
                    temp.append(last[index]+last[index-1])
                temp.append(1)
            last = temp
        return last


