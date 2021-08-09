# -*- coding:utf-8 -*-
# @Time    : 2021/8/9 8:39
# @Author  : zengln
# @File    : 丑数 II.py

# 给你一个整数 n ，请你找出并返回第 n 个 丑数 。
#
#  丑数 就是只包含质因数 2、3 和/或 5 的正整数。
#
#
#
#  示例 1：
#
#
# 输入：n = 10
# 输出：12
# 解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。
#
#
#  示例 2：
#
#
# 输入：n = 1
# 输出：1
# 解释：1 通常被视为丑数。
#
#
#
#
#  提示：
#
#
#  1 <= n <= 1690
#
#  Related Topics 哈希表 数学 动态规划 堆（优先队列）
#  👍 709 👎 0


class Solution:
    """
    丑数的计算：
    第一个丑数是1
    后面的丑数等于前面的丑数乘以(2,3,5)其中一个，其中最小的为下一个丑数
    """
    def nthUglyNumber(self, n: int) -> int:
        result = [1]
        p2 = 0
        p3 = 0
        p5 = 0
        # 加上一个while是为了防止出现重复偶数的情况，例如6：2X3 和 3X2都会出现一次，但是只能要一个
        for i in range(1, n):
            temp = 1
            while temp in result:
                temp = min(result[p2] * 2, result[p3] * 3, result[p5] * 5)
                if temp == result[p2] * 2:
                    p2 += 1
                elif temp == result[p3] * 3:
                    p3 += 1
                else:
                    p5 += 1
            result.append(temp)
        return result[-1]


# 其他人解决重复出现数字的问题写法
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        p2 = p3 = p5 = 1

        for i in range(2, n + 1):
            num2, num3, num5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(num2, num3, num5)
            if dp[i] == num2:
                p2 += 1
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1

        return dp[n]