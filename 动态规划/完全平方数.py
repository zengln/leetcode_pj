# -*- coding:utf-8 -*-
# @Time : 2021/8/21 11:39 
# @Author : zengln
# @File : 完全平方数.py 
# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
#
#  给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。
#
#  完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
#
#
#
#
#  示例 1：
#
#
# 输入：n = 12
# 输出：3
# 解释：12 = 4 + 4 + 4
#
#  示例 2：
#
#
# 输入：n = 13
# 输出：2
# 解释：13 = 4 + 9
#
#
#  提示：
#
#
#  1 <= n <= 104
#
#  Related Topics 广度优先搜索 数学 动态规划
#  👍 1048 👎 0



class Solution:
    """
    dp[i] i 表示到i的最少数量
    dp[i] = min(dp[i-平方数1], dp[i-平方数2])+1
    因为n小于105，所以最大的平方数也就时100，平方数个数时确定的(不确定估计时hard难度)
    边界值dp[0] = 0

    妈的，题目范围是放屁啊，有个测试用例n是121
    """
    def numSquares(self, n: int) -> int:
        nums = []
        temp = 1
        temp_2 = 1
        while temp_2 <= n:
            nums.append(temp_2)
            temp += 1
            temp_2 = temp * temp

        dp = [float(inf)] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            for j in nums:
                if i - j < 0:
                    break
                dp[i] = min(dp[i], dp[i-j] + 1)
        return dp[-1]


