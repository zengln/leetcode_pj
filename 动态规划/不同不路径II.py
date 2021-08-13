# -*- coding:utf-8 -*-
# @Time    : 2021/8/13 10:13
# @Author  : zengln
# @File    : 不同不路径II.py

# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
#
#  机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
#
#  现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
#
#
#
#  网格中的障碍物和空位置分别用 1 和 0 来表示。
#
#
#
#  示例 1：
#
#
# 输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# 输出：2
# 解释：
# 3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右
#
#
#  示例 2：
#
#
# 输入：obstacleGrid = [[0,1],[0,0]]
# 输出：1
#
#
#
#
#  提示：
#
#
#  m == obstacleGrid.length
#  n == obstacleGrid[i].length
#  1 <= m, n <= 100
#  obstacleGrid[i][j] 为 0 或 1
#
#  Related Topics 数组 动态规划 矩阵
#  👍 602 👎 0



class Solution:
    """
    使用一个二维数dp组保存到当前点(i,j)的路径个数
    当前点可能从 (i-1,j)向下移动或者(i,j-1)向右移动得到
    dp[i][j] = dp[i-1][j] + dp[i][j-1]
    dp[0][0] = 1
    i = 0
    dp[i][j] = dp[i][j-1]
    j = 0
    dp[i][j] = dp[i-1][j]
    如果obstacleGrid[i][j] = 1,那么dp[i][j] = 0
    """
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0] * len(obstacleGrid[i]) for i in range(len(obstacleGrid))]
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[i])):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue

                if i == 0 and j == 0:
                    dp[0][0] = 1
                elif i == 0:
                    dp[i][j] = dp[i][j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]


