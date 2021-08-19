# -*- coding:utf-8 -*-
# @Time    : 2021/8/19 17:35
# @Author  : zengln
# @File    : 零钱兑换.py

# 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
#
#  计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
#
#  你可以认为每种硬币的数量是无限的。
#
#
#
#  示例 1：
#
#
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3
# 解释：11 = 5 + 5 + 1
#
#  示例 2：
#
#
# 输入：coins = [2], amount = 3
# 输出：-1
#
#  示例 3：
#
#
# 输入：coins = [1], amount = 0
# 输出：0
#
#
#  示例 4：
#
#
# 输入：coins = [1], amount = 1
# 输出：1
#
#
#  示例 5：
#
#
# 输入：coins = [1], amount = 2
# 输出：2
#
#
#
#
#  提示：
#
#
#  1 <= coins.length <= 12
#  1 <= coins[i] <= 231 - 1
#  0 <= amount <= 104
#
#  Related Topics 广度优先搜索 数组 动态规划
#  👍 1428 👎 0



class Solution:
    """

    dp[i] 为到i元需要的最小硬币个数
    dp[i] = min(dp[i-coint1], dp[i-conint2], dp[i-coint3])+1
    dp[0] = 0
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount+1):
            min_count = -1
            for j in coins:
                if i < j:
                    continue

                if dp[i-j] == -1:
                    continue
                elif min_count == -1 or dp[i-j] + 1 < min_count:
                    min_count = dp[i-j] + 1

            dp[i] = min_count
        # print(dp)
        return dp[-1]

