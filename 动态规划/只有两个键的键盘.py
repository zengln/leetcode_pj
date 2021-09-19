# -*- coding:utf-8 -*-
# @Time : 2021/9/19 15:14 
# @Author : zengln
# @File : 只有两个键的键盘.py 
# 最初记事本上只有一个字符 'A' 。你每次可以对这个记事本进行两种操作：
#
#
#  Copy All（复制全部）：复制这个记事本中的所有字符（不允许仅复制部分字符）。
#  Paste（粘贴）：粘贴 上一次 复制的字符。
#
#
#  给你一个数字 n ，你需要使用最少的操作次数，在记事本上输出 恰好 n 个 'A' 。返回能够打印出 n 个 'A' 的最少操作次数。
#
#
#
#  示例 1：
#
#
# 输入：3
# 输出：3
# 解释：
# 最初, 只有一个字符 'A'。
# 第 1 步, 使用 Copy All 操作。
# 第 2 步, 使用 Paste 操作来获得 'AA'。
# 第 3 步, 使用 Paste 操作来获得 'AAA'。
#
#
#  示例 2：
#
#
# 输入：n = 1
# 输出：0
#
#
#
#
#  提示：
#
#
#  1 <= n <= 1000
#
#  Related Topics 数学 动态规划
#  👍 361 👎 0


class Solution:
    """
    dp[i] 为有N个字符时，操作的次数
    dp[1] = 0
    dp[0] = 0
    dp[2] = 2
    dp[3] = 3
    dp[4] = 4
    dp[5] = 5
    dp[6] = 5
    dp[7] = 7
    dp[8] = 6
    dp[9] = 6
    dp[n]
    找到1-n/2中, 约数,找到最小值
    """
    def minSteps(self, n: int) -> int:
        dp = [i for i in range(n+1)]
        dp[0] = 0
        dp[1] = 0
        if n < 2:
            return dp[n]
        for i in range(4, n+1):
            for j in range(2, (i//2)+1):
                if i % j == 0:
                    dp[i] = min(dp[j] + dp[i//j], dp[i])

        return dp[-1]

