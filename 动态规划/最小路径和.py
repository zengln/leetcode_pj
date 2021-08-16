# -*- coding:utf-8 -*-
# @Time : 2021/8/14 17:36 
# @Author : zengln
# @File : 最小路径和.py 
# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
#  说明：每次只能向下或者向右移动一步。
#
#
#
#  示例 1：
#
#
# 输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
# 输出：7
# 解释：因为路径 1→3→1→1→1 的总和最小。
#
#
#  示例 2：
#
#
# 输入：grid = [[1,2,3],[4,5,6]]
# 输出：12
#
#
#
#
#  提示：
#
#
#  m == grid.length
#  n == grid[i].length
#  1 <= m, n <= 200
#  0 <= grid[i][j] <= 100
#
#  Related Topics 数组 动态规划 矩阵
#  👍 958 👎 0



class Solution:
    """
    当前点(i,j)的路径和为：
    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    边界：
    i = 0
    dp[i][j] = dp[i][j-1] + grid[i][j]
    j = 0
    dp[i][j] = dp[i-1][j] + grid[i][j]
    """
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        result = [[0] * (n) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    result[i][j] = grid[0][0]
                elif i == 0:
                    result[i][j] = result[i][j-1] + grid[i][j]
                elif j == 0:
                    result[i][j] = result[i-1][j] + grid[i][j]
                else:
                    result[i][j] = min(result[i][j-1], result[i-1][j]) + grid[i][j]

        return result[-1][-1]

