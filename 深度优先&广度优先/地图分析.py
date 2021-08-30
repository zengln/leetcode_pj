# -*- coding:utf-8 -*-
# @Time    : 2021/8/30 16:30
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
    广度优先
    """
    def maxDistance(self, grid: List[List[int]]) -> int:
        result = -1
        m, n = len(grid), len(grid[0])
        dist = [[0] * n for _ in range(m)]
        queue = [(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1]
        seen = set(queue)
        while queue:
            temp_x, temp_y = queue.pop(0)
            for x, y in [(temp_x+1, temp_y), (temp_x-1, temp_y), (temp_x, temp_y+1), (temp_x, temp_y-1)]:
                if 0 <= x < m and 0 <= y < n and (x, y) not in seen:
                    dist[x][y] = dist[temp_x][temp_y] + 1
                    seen.add((x, y))
                    queue.append((x, y))
                    if dist[x][y] > result:
                        result = dist[x][y]
        # print(dist)
        return result

