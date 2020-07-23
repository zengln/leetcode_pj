# -*- coding:utf-8 -*-
# @Time    : 2020/7/23 14:05
# @Author  : zengln
# @File    : 每日温度.py

# 请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。
#
#
#  例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2
# , 1, 1, 0, 0]。
#
#  提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。
#  Related Topics 栈 哈希表

from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result = [0] * len(T)
        stack = []
        stack.append([T[0], 0])

        for index in range(1, len(T)):
            while stack and stack[-1][0] < T[index]:
                result[stack[-1][1]] = index - stack[-1][1]
                stack.pop()

            stack.append([T[index], index])

        return result

s = Solution()
print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))



