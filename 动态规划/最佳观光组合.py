# -*- coding:utf-8 -*-
# @Time    : 2021/8/5 13:22
# @Author  : zengln
# @File    : 最佳观光组合.py

# 给你一个正整数数组 values，其中 values[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的 距离 为 j - i。
#
#  一对景点（i < j）组成的观光组合的得分为 values[i] + values[j] + i - j ，也就是景点的评分之和 减去 它们两者之间的距离
# 。
#
#  返回一对观光景点能取得的最高分。
#
#
#
#  示例 1：
#
#
# 输入：values = [8,1,5,2,6]
# 输出：11
# 解释：i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11
#
#
#  示例 2：
#
#
# 输入：values = [1,2]
# 输出：2
#
#
#
#
#  提示：
#
#
#  2 <= values.length <= 5 * 104
#  1 <= values[i] <= 1000
#
#  Related Topics 数组 动态规划
#  👍 208 👎 0



class Solution:
    """
    某一对观光景点的得分：
    dp_start[i] = value[i] + i
    dp_end[j] = value[j] - j
    i < j
    算出最大值。解法超时

    -------------
    用一个数组
    记录到此为止的起点最大值
    dp_start[i] = max(value[i] + i, dp_start[i-1])

    最大观光值
    temp= dp_start[i] - j + value[j]
    ------------------
    用一个数组记录到此为终点的最大值
    dp_end[i] = max(value[i] - i, dp_end[i-1])
    --------------------
    """
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_value = 0
        result = [0] * len(values)
        result[0] = values[0]
        for i in range(1, len(values)):
            temp = values[i] - i + result[i-1]
            result[i] = max(result[i-1], values[i]+i)
            max_value = max(max_value, temp)
        return max_value


