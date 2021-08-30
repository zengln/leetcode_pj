# -*- coding:utf-8 -*-
# @Time    : 2021/8/30 10:18
# @Author  : zengln
# @File    : 图像渲染.py

# 有一幅以二维整数数组表示的图画，每一个整数表示该图画的像素值大小，数值在 0 到 65535 之间。
#
#  给你一个坐标 (sr, sc) 表示图像渲染开始的像素值（行 ，列）和一个新的颜色值 newColor，让你重新上色这幅图像。
#
#  为了完成上色工作，从初始坐标开始，记录初始坐标的上下左右四个方向上像素值与初始坐标相同的相连像素点，接着再记录这四个方向上符合条件的像素点与他们对应四个方
# 向上像素值与初始坐标相同的相连像素点，……，重复该过程。将所有有记录的像素点的颜色值改为新的颜色值。
#
#  最后返回经过上色渲染后的图像。
#
#  示例 1:
#
#
# 输入:
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1, sc = 1, newColor = 2
# 输出: [[2,2,2],[2,2,0],[2,0,1]]
# 解析:
# 在图像的正中间，(坐标(sr,sc)=(1,1)),
# 在路径上所有符合条件的像素点的颜色都被更改成2。
# 注意，右下角的像素没有更改为2，
# 因为它不是在上下左右四个方向上与初始点相连的像素点。
#
#
#  注意:
#
#
#  image 和 image[0] 的长度在范围 [1, 50] 内。
#  给出的初始点将满足 0 <= sr < image.length 和 0 <= sc < image[0].length。
#  image[i][j] 和 newColor 表示的颜色值在范围 [0, 65535]内。
#
#  Related Topics 深度优先搜索 广度优先搜索 数组 矩阵
#  👍 210 👎 0



class Solution:
    """
    深度优先，从起始点开始, 上下左右开始遍历，如果当前点在矩阵范围内，且颜色不等于替换色，那么当前点就是需要替换的点
    先替换颜色，然后再次开始上下左右遍历。(这样可以防止一个点被重复遍历)
    """
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        temp = image[sr][sc]
        r, c = len(image), len(image[0])
        def dfs(x, y):
            if image[x][y] == temp:
                image[x][y] = newColor
                for x, y in [(x-1, y), (x+1, y), (x, y+1), (x, y-1)]:
                    if 0 <= x < r and 0 <= y < c and image[x][y] != newColor:
                        dfs(x, y)
            return
        if temp != newColor:
            dfs(sr, sc)
        return image

import collections

class Solution:
    """
    广度优先：从初始点开始，上下左右遍历，确认符合条件的点后，将其加入到队列中，然后将当前点更改为新颜色
    """
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        temp = image[sr][sc]
        r, c = len(image), len(image[0])

        if temp == newColor:
            return image
        image[sr][sc] = newColor
        queue = collections.deque([(sr, sc)])
        while queue:
            x, y = queue.popleft()
            for x, y in [(x-1, y), (x+1, y), (x, y+1), (x, y-1)]:
                if 0 <= x < r and 0 <= y < c and image[x][y] == temp:
                    queue.append((x, y))
                    image[x][y] = newColor
            print(queue)
        return image
"""
目前观察到的深度遍历与广度遍历的区别：
深度使用递归，从一个点开始一直往下
广度使用队列，走完一个点后，将当前点关联的数据暂存在队列中，按照进入队列的顺序往下走
"""
