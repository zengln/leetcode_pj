# -*- coding:utf-8 -*-
# @Time    : 2021/8/30 18:10
# @Author  : zengln
# @File    : 腐烂的橘子.py

# 在给定的网格中，每个单元格可以有以下三个值之一：
#
#
#  值 0 代表空单元格；
#  值 1 代表新鲜橘子；
#  值 2 代表腐烂的橘子。
#
#
#  每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。
#
#  返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。
#
#
#
#  示例 1：
#
#
#
#  输入：[[2,1,1],[1,1,0],[0,1,1]]
# 输出：4
#
#
#  示例 2：
#
#  输入：[[2,1,1],[0,1,1],[1,0,1]]
# 输出：-1
# 解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。
#
#
#  示例 3：
#
#  输入：[[0,2]]
# 输出：0
# 解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
#
#
#
#
#  提示：
#
#
#  1 <= grid.length <= 10
#  1 <= grid[0].length <= 10
#  grid[i][j] 仅为 0、1 或 2
#
#  Related Topics 广度优先搜索 数组 矩阵
#  👍 404 👎 0



class Solution:
    """
    找到所有腐烂的橘子
    所有腐烂的橘子往上下左右扩散，扩散到的新鲜橘子转成腐烂的橘子，并且记时间为1
    新转成腐烂的橘子再往外扩散，直到能扩散到的位置都扩散完毕

    找列表中是否在新鲜橘子，存在返回-1
    不存在返回时间
    """
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        result = 0
        queue = list()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
        while queue:
            i, j, result = queue.pop(0)
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    grid[x][y] = 2
                    queue.append((x, y, result+1))

        for i in grid:
            if 1 in i:
                return -1
        return result

