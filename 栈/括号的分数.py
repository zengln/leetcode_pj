# -*- coding:utf-8 -*-
# @Time    : 2020/7/24 11:17
# @Author  : zengln
# @File    : 括号的分数.py

# 给定一个平衡括号字符串 S，按下述规则计算该字符串的分数：
#
#
#  () 得 1 分。
#  AB 得 A + B 分，其中 A 和 B 是平衡括号字符串。
#  (A) 得 2 * A 分，其中 A 是平衡括号字符串。
#
#
#
#
#  示例 1：
#
#  输入： "()"
# 输出： 1
#
#
#  示例 2：
#
#  输入： "(())"
# 输出： 2
#
#
#  示例 3：
#
#  输入： "()()"
# 输出： 2
#
#
#  示例 4：
#
#  输入： "(()(()))"
# 输出： 6
#
#
#
#
#  提示：
#
#
#  S 是平衡括号字符串，且只含有 ( 和 ) 。
#  2 <= S.length <= 50
#
#  Related Topics 栈 字符串


class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        for x in S:
            while x == ")" and stack:
                tmp = stack.pop()
                if tmp == "(":
                    stack.append(1)
                    break
                elif isinstance(tmp, int) and stack[-1] == "(":
                    stack.pop()
                    stack.append(2 * tmp)
                    break
                elif isinstance(tmp, int) and isinstance(stack[-1], int):
                    stack.append(tmp + stack.pop())
            if x != ")":
                stack.append(x)
        sum = 0
        for x in stack:
            sum += x

        return sum

s = Solution()
print(s.scoreOfParentheses("()"))
print(s.scoreOfParentheses("(())"))
print(s.scoreOfParentheses("()()"))
print(s.scoreOfParentheses("(()(()))"))




