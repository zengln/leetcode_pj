# -*- coding:utf-8 -*-
# @Time    : 2021/7/29 8:24
# @Author  : zengln
# @File    : 三步问题.py

# 三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。实现一种方法，计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模100
# 0000007。
#
#  示例1:
#
#
#  输入：n = 3
#  输出：4
#  说明: 有四种走法
#
#
#  示例2:
#
#
#  输入：n = 5
#  输出：13
#
#
#  提示:
#
#
#  n范围在[1, 1000000]之间
#
#  Related Topics 记忆化搜索 数学 动态规划



class Solution:
    def waysToStep(self, n: int) -> int:
        """
        假设当前台阶为N，那么它可能是
        N-1
        N-2
        N-3
        这三种情况个台阶上来的，总共4种情况
        """
        if n <= 2:
            return n

        if n == 3:
            return 4
        a, b, c = 1, 2, 4
        for i in range(4, n+1):
            tmp = (a + b + c) % 1000000007
            a, b, c = b, c, tmp
        return c

