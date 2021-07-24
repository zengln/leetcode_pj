# -*- coding:utf-8 -*-
# @Time : 2021/7/24 15:37 
# @Author : zengln
# @File : 使用最小花费爬楼梯.py 
# 数组的每个下标作为一个阶梯，第 i 个阶梯对应着一个非负数的体力花费值 cost[i]（下标从 0 开始）。
#
#  每当你爬上一个阶梯你都要花费对应的体力值，一旦支付了相应的体力值，你就可以选择向上爬一个阶梯或者爬两个阶梯。
#
#  请你找出达到楼层顶部的最低花费。在开始时，你可以选择从下标为 0 或 1 的元素作为初始阶梯。
#
#
#
#  示例 1：
#
#
# 输入：cost = [10, 15, 20]
# 输出：15
# 解释：最低花费是从 cost[1] 开始，然后走两步即可到阶梯顶，一共花费 15 。
#
#
#  示例 2：
#
#
# 输入：cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# 输出：6
# 解释：最低花费方式是从 cost[0] 开始，逐个经过那些 1 ，跳过 cost[3] ，一共花费 6 。
#
#
#
#
#  提示：
#
#
#  cost 的长度范围是 [2, 1000]。
#  cost[i] 将会是一个整型数据，范围为 [0, 999] 。
#
#  Related Topics 数组 动态规划

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''

        这是动态规划题
        假如当前在第i个阶梯，那么它可能是上了一步或者两步过来的，那么到本台阶所使用的体力
        d[i] = min（d[i-1]+cost[i-1], d[i-2]+cost[i-2]）
        边界值 d[0],d[1]
        '''
        d = [-1] * (len(cost) + 1)
        d[0] = 0
        d[1] = 0
        for i in range(2, len(cost)+1):
            d[i] = min(d[i-1]+cost[i-1], d[i-2]+cost[i-2])

        return d[len(cost)]



class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''

        这是动态规划题
        假如当前在第i个阶梯，那么它可能是上了一步或者两步过来的
        d[i] = min（d[i-1]+d[i], d[i-2]+d[i]）
        边界值 d[0],d[1]
        '''
        d = [-1] * len(cost)
        d[0] = cost[0]
        d[1] = cost[1]
        for i in range(2, len(cost)):
            d[i] = min(d[i-1]+cost[i], d[i-2]+cost[i])

        if d[-2] < d[-1]:
            return d[-2]
        else:
            return d[-1]