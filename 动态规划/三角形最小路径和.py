# -*- coding:utf-8 -*-
# @Time    : 2021/8/11 16:19
# @Author  : zengln
# @File    : 三角形最小路径和.py

# 给定一个三角形 triangle ，找出自顶向下的最小路径和。
#
#  每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。也就是说，如果
# 正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。
#
#
#
#  示例 1：
#
#
# 输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# 输出：11
# 解释：如下面简图所示：
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
#
#
#  示例 2：
#
#
# 输入：triangle = [[-10]]
# 输出：-10
#
#
#
#
#  提示：
#
#
#  1 <= triangle.length <= 200
#  triangle[0].length == 1
#  triangle[i].length == triangle[i - 1].length + 1
#  -104 <= triangle[i][j] <= 104
#
#
#
#
#  进阶：
#
#
#  你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题吗？
#
#  Related Topics 数组 动态规划
#  👍 810 👎 0



class Solution:
    """
    和931.下降路径最小和差不多的思路
    算出到每一个数最小的和，找出最后一行最小的数
    第i行第j个数的最小和
    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
    """
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        result = [triangle[0]]
        for i in range(1, len(triangle)):
            temp = []
            for j in range(len(triangle[i])):
                if j == 0:
                    min_value = result[-1][0]
                elif j == len(triangle[i]) - 1:
                    min_value = result[-1][-1]
                else:
                    min_value = min(result[-1][j], result[-1][j-1])
                temp.append(min_value + triangle[i][j])
            result.append(temp)

        return min(result[-1])


# 自顶向下，使用一维数组的优化写法
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        result = [0] * n
        result[0] = triangle[0][0]
        for i in range(1, n):
            for j in range(len(triangle[i])-1, -1, -1):
                if j == len(triangle[i]) - 1:
                    result[j] = result[j-1] + triangle[i][j]
                elif j == 0:
                    result[0] = result[0] + triangle[i][j]
                else:
                    result[j] = min(result[j], result[j-1]) + triangle[i][j]
        return min(result)

# 自下向上，一维数组
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        result = triangle[-1]
        for i in range(n-2, -1, -1):
            for j in range(len(triangle[i])):
                result[j] = min(result[j], result[j+1]) + triangle[i][j]
        return result[0]