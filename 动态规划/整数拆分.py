# -*- coding:utf-8 -*-
# @Time : 2021/8/21 12:17 
# @Author : zengln
# @File : 整数拆分.py 
# 给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。
#
#  示例 1:
#
#  输入: 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1。
#
#  示例 2:
#
#  输入: 10
# 输出: 36
# 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
#
#  说明: 你可以假设 n 不小于 2 且不大于 58。
#  Related Topics 数学 动态规划



class Solution:
    """
    dp[i]表示值为i时的最大乘积
    n 可以拆分成k与n-k
    若：n-k>1，则可以继续拆分，此时dp[n] = k * dp[n-k]
    n-k == 1,则dp[n] = k * (n-k)
    所以dp[n] = max(k * (n-k),k * dp[n-k])

    """
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], max(j * (i-j), j * dp[i-j]))

        return dp[-1]

