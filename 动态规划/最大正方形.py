# -*- coding:utf-8 -*-
# @Time : 2021/8/14 18:31 
# @Author : zengln
# @File : 最大正方形.py 
# 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
#
#
#
#  示例 1：
#
#
# 输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"]
# ,["1","0","0","1","0"]]
# 输出：4
#
#
#  示例 2：
#
#
# 输入：matrix = [["0","1"],["1","0"]]
# 输出：1
#
#
#  示例 3：
#
#
# 输入：matrix = [["0"]]
# 输出：0
#
#
#
#
#  提示：
#
#
#  m == matrix.length
#  n == matrix[i].length
#  1 <= m, n <= 300
#  matrix[i][j] 为 '0' 或 '1'
#
#  Related Topics 数组 动态规划 矩阵
#  👍 836 👎 0



class Solution:
    """
    max_result保存最大正方形的边长
    维护一个二维数组,保存以当前点为右下角的正方形的边长
    那么，当前点(i,j)的最大边长为以i,j为右下角,(i-1,j),(i-1,j-1)和(i,j-1)里最小值加一
    dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+1
    边界值：
    i = 0 or j = 0
    dp[0][j] = min(1, matrix[i][j])
    """
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        result = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        max_result = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] != "1":
                    continue

                if i == 0 or j == 0:
                    temp = 1
                else:
                    temp = min(result[i][j-1], result[i-1][j-1], result[i-1][j]) + 1

                result[i][j] = temp
                if temp > max_result:
                    max_result = temp
        return max_result * max_result




