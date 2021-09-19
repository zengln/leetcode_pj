# -*- coding:utf-8 -*-
# @Time    : 2021/9/13 13:26
# @Author  : zengln
# @File    : 回旋镖的数量.py

# 给定平面上 n 对 互不相同 的点 points ，其中 points[i] = [xi, yi] 。回旋镖 是由点 (i, j, k) 表示的元组 ，其中
#  i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。
#
#  返回平面上所有回旋镖的数量。
#
#
#  示例 1：
#
#
# 输入：points = [[0,0],[1,0],[2,0]]
# 输出：2
# 解释：两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]
#
#
#  示例 2：
#
#
# 输入：points = [[1,1],[2,2],[3,3]]
# 输出：2
#
#
#  示例 3：
#
#
# 输入：points = [[1,1]]
# 输出：0
#
#
#
#
#  提示：
#
#
#  n == points.length
#  1 <= n <= 500
#  points[i].length == 2
#  -104 <= xi, yi <= 104
#  所有点都 互不相同
#
#  Related Topics 数组 哈希表 数学

class Solution:
    """
    遍历每个点，计算这个点与其他点的记录，将记录记录在dict中
    """
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        result = 0
        for i in range(len(points)):
            temp = dict()
            for j in range(len(points)):
                if i == j:
                    continue

                x = points[i][0] - points[j][0]
                y = points[i][1] - points[j][1]
                dist = x * x + y * y
                temp[dist] = temp.get(dist, 0) + 1

            for key in temp.keys():
                nums = temp.get(key)
                result += nums * (nums-1)
        return result


