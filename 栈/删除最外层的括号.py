# -*- coding:utf-8 -*-
# @Time    : 2020/7/7 19:50
# @Author  : zengln
# @File    : 删除最外层的括号.py

# 有效括号字符串为空 ("")、"(" + A + ")" 或 A + B，其中 A 和 B 都是有效的括号字符串，+ 代表字符串的连接。例如，""，"()"
# ，"(())()" 和 "(()(()))" 都是有效的括号字符串。
#
#  如果有效字符串 S 非空，且不存在将其拆分为 S = A+B 的方法，我们称其为原语（primitive），其中 A 和 B 都是非空有效括号字符串。
#
#  给出一个非空有效字符串 S，考虑将其进行原语化分解，使得：S = P_1 + P_2 + ... + P_k，其中 P_i 是有效括号字符串原语。
#
#  对 S 进行原语化分解，删除分解中每个原语字符串的最外层括号，返回 S 。
#
#
#
#  示例 1：
#
#  输入："(()())(())"
# 输出："()()()"
# 解释：
# 输入字符串为 "(()())(())"，原语化分解得到 "(()())" + "(())"，
# 删除每个部分中的最外层括号后得到 "()()" + "()" = "()()()"。
#
#  示例 2：
#
#  输入："(()())(())(()(()))"
# 输出："()()()()(())"
# 解释：
# 输入字符串为 "(()())(())(()(()))"，原语化分解得到 "(()())" + "(())" + "(()(()))"，
# 删除每个部分中的最外层括号后得到 "()()" + "()" + "()(())" = "()()()()(())"。
#
#
#  示例 3：
#
#  输入："()()"
# 输出：""
# 解释：
# 输入字符串为 "()()"，原语化分解得到 "()" + "()"，
# 删除每个部分中的最外层括号后得到 "" + "" = ""。
#
#
#
#
#  提示：
#
#
#  S.length <= 10000
#  S[i] 为 "(" 或 ")"
#  S 是一个有效括号字符串
#

class Solution1:
    def removeOuterParentheses(self, S: str) -> str:
        left = 0
        right = 0
        stack = []
        result = ""
        for x in S:
            if x == "(":
                left += 1
            else:
                right += 1
            stack.append(x)
            if left == right and len(stack) != 2:
                print(stack)
                result += ''.join(stack[1:-1])
                stack = []
                left = 0
                right = 0
            elif left == right:
                print(stack)
                stack = []
                left = 0
                right = 0
        return result


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        num = 0
        result = ""
        for x in S:

            if x == "(":
                num += 1
                if num > 1:
                    result += x
            else:
                num -= 1
                if num > 0:
                    result += x

        return result

s = Solution()
print(s.removeOuterParentheses("(()())(())"))