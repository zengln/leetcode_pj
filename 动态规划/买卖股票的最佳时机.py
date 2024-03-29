# -*- coding:utf-8 -*-
# @Time : 2021/7/20 19:55 
# @Author : zengln
# @File : 买卖股票的最佳时机.py 
# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
#
#  你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
#
#  返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
#
#
#
#  示例 1：
#
#
# 输入：[7,1,5,3,6,4]
# 输出：5
# 解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
#
#
#  示例 2：
#
#
# 输入：prices = [7,6,4,3,1]
# 输出：0
# 解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
#
#
#
#
#  提示：
#
#
#  1 <= prices.length <= 105
#  0 <= prices[i] <= 104
#
#  Related Topics 数组 动态规划


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        result = 0
        for i in prices:
            if buy_price > i:
                buy_price = i
            else:
                temp = i - buy_price
                if temp > result:
                    result = temp

        return result

'''
假设第一天价格为买入价，初始化利润为0
若：第二天价格比买入小，则第二天价格为买入
第三天价格比买入小，则第三天价格买入
。。。
直到第N天，价格比买入大，计算结果为当前最大利润。
后续出现更小的买入价，则替换买入价，找到这个买入价格之后的最大利润，没有则之前计算利润为最大利润。

'''
# 更新第二次做的解法
class Solution:
    """
    找到最大利润
    当天卖出 = max(前一天最大的卖出利润，当天卖出利润)
    dp[i] = max(dp[i-1], prices[i] - buy)
    """
    def maxProfit(self, prices: List[int]) -> int:
        result = [0] * len(prices)
        buy = prices[0]
        for i in range(1, len(prices)):
            result[i] = max(result[i-1], prices[i] - buy)
            buy = min(prices[i], buy)
        return result[-1]