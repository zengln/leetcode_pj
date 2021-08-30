# -*- coding:utf-8 -*-
# @Time    : 2021/8/30 16:09
# @Author  : zengln
# @File    : 地图分析.py

# 你现在手里有一份大小为 N x N 的 网格 grid，上面的每个 单元格 都用 0 和 1 标记好了。其中 0 代表海洋，1 代表陆地，请你找出一个海洋单
# 元格，这个海洋单元格到离它最近的陆地单元格的距离是最大的。
#
#  我们这里说的距离是「曼哈顿距离」（ Manhattan Distance）：(x0, y0) 和 (x1, y1) 这两个单元格之间的距离是 |x0 -
# x1| + |y0 - y1| 。
#
#  如果网格上只有陆地或者海洋，请返回 -1。
#
#
#
#  示例 1：
#
#
#
#  输入：[[1,0,1],[0,0,0],[1,0,1]]
# 输出：2
# 解释：
# 海洋单元格 (1, 1) 和所有陆地单元格之间的距离都达到最大，最大距离为 2。
#
#
#  示例 2：
#
#
#
#  输入：[[1,0,0],[0,0,0],[0,0,0]]
# 输出：4
# 解释：
# 海洋单元格 (2, 2) 和所有陆地单元格之间的距离都达到最大，最大距离为 4。
#
#
#
#
#  提示：
#
#
#  1 <= grid.length == grid[0].length <= 100
#  grid[i][j] 不是 0 就是 1
#
#  Related Topics 广度优先搜索 数组 动态规划 矩阵

class Solution:
    """
    dp[i][j]表示点(i,j)到距离他最近的陆地的距离
    grid[i][j] 为1
    dp[i][j] = 0
    grid[i][j] = 0
    dp[i][j] = min(dp[i-1][j],dp[i+1][j], dp[i][j+1], dp[i][j-1) + 1
    return max(dp)
    """
    def maxDistance(self, grid: List[List[int]]) -> int:
        result = -1
        m, n = len(grid), len(grid[0])
        dp = [[float(inf)] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if i > 0 and j > 0:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
                    elif i > 0:
                        dp[i][j] = dp[i-1][j] + 1
                    elif j > 0:
                        dp[i][j] = dp[i][j-1] + 1
                else:
                    dp[i][j] = 0

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if grid[i][j] == 0:
                    if i < m-1 and j < n - 1:
                        dp[i][j] = min(min(dp[i+1][j], dp[i][j+1]) + 1, dp[i][j])
                    elif i < m-1:
                        dp[i][j] = min(dp[i+1][j] + 1, dp[i][j])
                    elif j < n-1:
                        dp[i][j] = min(dp[i][j+1] + 1, dp[i][j])

                if dp[i][j] > result:
                    result = dp[i][j]
        if result == 0 or result == float(inf):
            return -1
        else:
            return result


