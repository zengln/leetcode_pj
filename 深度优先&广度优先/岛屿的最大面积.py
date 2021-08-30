# -*- coding:utf-8 -*-
# @Time    : 2021/8/30 11:05
# @Author  : zengln
# @File    : 岛屿的最大面积.py

# 给定一个包含了一些 0 和 1 的非空二维数组 grid 。
#
#  一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设 grid 的四个边缘都被
# 0（代表水）包围着。
#
#  找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。)
#
#
#
#  示例 1:
#
#  [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
#
#
#  对于上面这个给定矩阵应返回 6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。
#
#  示例 2:
#
#  [[0,0,0,0,0,0,0,0]]
#
#  对于上面这个给定的矩阵, 返回 0。
#
#
#
#  注意: 给定的矩阵grid 的长度和宽度都不超过 50。
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵
#  👍 542 👎 0



class Solution:
    """
    遍历所有的点，当当前点为1时，计算当前点关联到的岛屿的面积
    岛屿面积计算能使用深度优先
    """
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        r, c = len(grid), len(grid[0])
        """
        计算(x,y)点相关的岛屿面积
        """
        def dfs(x, y):
            temp = 1
            for x, y in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0 <= x < r and 0 <= y < c and grid[x][y] == 1:
                    grid[x][y] = 0
                    temp += dfs(x, y)
            return temp


        for x in range(r):
            for y in range(c):
                if grid[x][y] == 1:
                    grid[x][y] = 0
                    temp = dfs(x, y)
                    if temp > result:
                        result = temp

        return result

class Solution:
    """
    遍历所有的点，当当前点为1时，计算当前点关联到的岛屿的面积
    岛屿面积计算能使用广度优先
    """
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        r, c = len(grid), len(grid[0])
        for x in range(r):
            for y in range(c):
                if grid[x][y] != 1:
                    continue
                queue = [(x, y)]
                grid[x][y] = 0
                temp = 1
                while queue:
                    x, y = queue.pop(0)
                    for x, y in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                        if 0 <= x < r and 0 <= y < c and grid[x][y] == 1:
                            temp += 1
                            grid[x][y] = 0
                            queue.append((x, y))
                result = max(result, temp)

        return result
