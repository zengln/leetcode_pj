# -*- coding:utf-8 -*-
# @Time    : 2020/7/20 19:32
# @Author  : zengln
# @File    : 132模式.py

# 给定一个整数序列：a1, a2, ..., an，一个132模式的子序列 ai, aj, ak 被定义为：当 i < j < k 时，ai < ak < a
# j。设计一个算法，当给定有 n 个数字的序列时，验证这个序列中是否含有132模式的子序列。
#
#  注意：n 的值小于15000。
#
#  示例1:
#
#
# 输入: [1, 2, 3, 4]
#
# 输出: False
#
# 解释: 序列中不存在132模式的子序列。
#
#
#  示例 2:
#
#
# 输入: [3, 1, 4, 2]
#
# 输出: True
#
# 解释: 序列中有 1 个132模式的子序列： [1, 4, 2].
#
#
#  示例 3:
#
#
# 输入: [-1, 3, 2, 0]
#
# 输出: True
#
# 解释: 序列中有 3 个132模式的的子序列: [-1, 3, 2], [-1, 3, 0] 和 [-1, 2, 0].

from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        mi = [nums[0]]
        stack = []
        for x in range(1, len(nums)):
            mi.append(min(mi[-1], x))

        for x in range(len(nums)-1, -1, -1):
            if not stack:
                stack.append(nums[x])
                continue



s = Solution()
s.find132pattern([-1, 3, 2, 0])