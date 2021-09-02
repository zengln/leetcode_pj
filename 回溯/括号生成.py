# -*- coding:utf-8 -*-
# @Time    : 2021/9/2 11:17
# @Author  : zengln
# @File    : 括号生成.py

# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
#  有效括号组合需满足：左括号必须以正确的顺序闭合。
#
#
#
#  示例 1：
#
#
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
#
#
#  示例 2：
#
#
# 输入：n = 1
# 输出：["()"]
#
#
#
#
#  提示：
#
#
#  1 <= n <= 8
#
#  Related Topics 字符串 动态规划 回溯

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(result, temp, left_count, right_count):
            if len(temp) == n * 2:
                result.append("".join(temp))

            if left_count < n:
                temp.append("(")
                dfs(result, temp, left_count + 1, right_count)
                temp.pop(-1)

            if right_count < left_count and right_count < n:
                temp.append(")")
                dfs(result, temp, left_count, right_count + 1)
                temp.pop(-1)

        result = []
        temp = []
        dfs(result, temp, 0, 0)
        return result


