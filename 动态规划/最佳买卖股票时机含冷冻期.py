# -*- coding:utf-8 -*-
# @Time    : 2021/8/6 8:30
# @Author  : zengln
# @File    : 最佳买卖股票时机含冷冻期.py

# 给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。
#
#  设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
#
#
#  你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#  卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
#
#
#  示例:
#
#  输入: [1,2,3,0,2]
# 输出: 3
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
#  Related Topics 数组 动态规划
#  👍 844 👎 0



class Solution:
    """
    第i天最大利润：
    手上有股票：
    dp_y[i]
    前一天有股票： dp_y[i] = dp_y[i-1]
    前一天没股票(一定是冷冻期) dp_y[i] = dp_l[i-1] - prices[i]
    手上没股票：
    前一天有股票： dp_n[i] = dp_y[i-1] + prices[i]
    前一天没股票： dp_n[i] = max(dp_n[i-1], dp_l[i-1])
    冷冻期：
    dp_l[i] = dp_n[i-1]
    """
    def maxProfit(self, prices: List[int]) -> int:
        dp_y = [0] * len(prices)
        dp_n = [0] * len(prices)
        dp_l = [0] * len(prices)
        dp_y[0] = -prices[0]
        for i in range(1, len(prices)):
            dp_y[i] = max(dp_y[i-1], dp_l[i-1] - prices[i])
            dp_n[i] = max(dp_y[i-1] + prices[i], dp_n[i-1], dp_l[i-1])
            dp_l[i] = dp_n[i-1]

        return dp_l[-1] if dp_l[-1] > dp_n[-1] else dp_n[-1]


