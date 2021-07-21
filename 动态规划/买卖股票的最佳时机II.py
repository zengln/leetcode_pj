# 给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。
#
#  设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
#
#  注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
#
#
#  示例 1:
#
#
# 输入: prices = [7,1,5,3,6,4]
# 输出: 7
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#      随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
#
#
#  示例 2:
#
#
# 输入: prices = [1,2,3,4,5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#      注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
#
#
#  示例 3:
#
#
# 输入: prices = [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
#
#
#
#  提示：
#
#
#  1 <= prices.length <= 3 * 104
#  0 <= prices[i] <= 104
#
#  Related Topics 贪心 数组 动态规划

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        # 贪心
        result = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                result += prices[i] - prices[i - 1]

        return result


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        动态规划：
        在第N天，最大的利润为前一天最大的利润，加上今天操作会取得的最大利润
        第N天分为两种情况：
        手上有股票,手上有股票,那么前一天可能：
        也有股票，今天没卖
        没有股票，今天买了,所以利润要减去今天买的金额
        取这两种情况下最大的利润值
        temp[N][1] = max(temp[N-1][1],temp[N-1][0]-price[N])
        手上没股票，那么前一天可能：
        也没股票，今天没买
        有股票，今天卖了
        temp[N][0] = max(temp[N-1][0], temp[N-1][1]+price[N])

        边界值第一天
        买股票 temp[0][1] = -price[0]
        不买 temp[0][0] = 0
        '''
        length = len(prices)
        result = [[-1, -1] for _ in range(length)]
        result[0][1] = -prices[0]
        result[0][0] = 0
        for i in range(1, length):
            result[i][0] = max(result[i-1][0], result[i-1][1]+prices[i])
            result[i][1] = max(result[i-1][1], result[i-1][0]-prices[i])

        return result[length-1][0]

