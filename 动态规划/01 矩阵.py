# -*- coding:utf-8 -*-
# @Time    : 2021/8/30 14:31
# @Author  : zengln
# @File    : 01 矩阵.py

# 给定一个由 0 和 1 组成的矩阵 mat ，请输出一个大小相同的矩阵，其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。
#
#  两个相邻元素间的距离为 1 。
#
#
#
#  示例 1：
#
#
#
#
# 输入：mat = [[0,0,0],[0,1,0],[0,0,0]]
# 输出：[[0,0,0],[0,1,0],[0,0,0]]
#
#
#  示例 2：
#
#
#
#
# 输入：mat = [[0,0,0],[0,1,0],[1,1,1]]
# 输出：[[0,0,0],[0,1,0],[1,2,1]]
#
#
#
#
#  提示：
#
#
#  m == mat.length
#  n == mat[i].length
#  1 <= m, n <= 104
#  1 <= m * n <= 104
#  mat[i][j] is either 0 or 1.
#  mat 中至少有一个 0
#
#  Related Topics 广度优先搜索 数组 动态规划 矩阵
#  👍 479 👎 0



class Solution:
    """
    dp[i][j]表示到点(i，j)到0的最小距离
    如果mat[i][j] = 0
    dp[i][j] = 0
    如果mat[i][j] = 1
    dp[i][j] = min(dp[i-1][j], dp[i+1][j], dp[i][j-1], dp[i][j+1])+1
    但是动态规划理论上，不会一个点上下左右的值都存在？
    所以要怎么算？
    ------
    分成两次计算：一次做从上开始算
    一次从右下开始算
    然后取最小值
    """
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        dp = [[float(inf)] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    if i > 0 and j > 0:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
                    elif i > 0:
                        dp[i][j] = dp[i-1][j] + 1
                    elif j > 0:
                        dp[i][j] = dp[i][j-1] + 1
                else:
                    dp[i][j] = 0

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if mat[i][j] == 1:
                    if i + 1 < n and j + 1 < m:
                        dp[i][j] = min(min(dp[i+1][j], dp[i][j+1]) + 1, dp[i][j])
                    elif i + 1 < n:
                        dp[i][j] = min(dp[i+1][j] + 1, dp[i][j])
                    elif j + 1 < m:
                        dp[i][j] = min(dp[i][j+1] + 1, dp[i][j])

        return dp


