# -*- coding:utf-8 -*-
# @Time    : 2021/1/13 19:50
# @Author  : zengln
# @File    : 字符串转证书(atoi).py

# 请你来实现一个 atoi 函数，使其能将字符串转换成整数。
#
#  首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。接下来的转化规则如下：
#
#
#  如果第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字字符组合起来，形成一个有符号整数。
#  假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成一个整数。
#  该字符串在有效的整数部分之后也可能会存在多余的字符，那么这些字符可以被忽略，它们对函数不应该造成影响。
#
#
#  假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换，即无法进行有效转换。
#
#  在任何情况下，若函数不能进行有效的转换时，请返回 0 。
#
#  注意：
#
#
#  本题中的空白字符只包括空格字符 ' ' 。
#  假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231, 231 − 1]。如果数值超过这个范围，请返回 231 − 1 或 −2
# 31 。
#
#
#
#
#  示例 1:
#
#
# 输入: "42"
# 输出: 42
#
#
#  示例 2:
#
#
# 输入: "   -42"
# 输出: -42
# 解释: 第一个非空白字符为 '-', 它是一个负号。
#      我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
#
#
#  示例 3:
#
#
# 输入: "4193 with words"
# 输出: 4193
# 解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。
#
#
#  示例 4:
#
#
# 输入: "words and 987"
# 输出: 0
# 解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
#      因此无法执行有效的转换。
#
#  示例 5:
#
#
# 输入: "-91283472332"
# 输出: -2147483648
# 解释: 数字 "-91283472332" 超过 32 位有符号整数范围。
#      因此返回 INT_MIN (−231) 。
#
#
#
#
#  提示：
#
#
#  0 <= s.length <= 200
#  s 由英文字母（大写和小写）、数字、' '、'+'、'-' 和 '.' 组成
#


class Solution:
    def myAtoi(self, s: str) -> int:
        result_list = []
        for s_char in s:

            if '0' <= s_char <= '9':
                result_list.append(s_char)
            elif not result_list and s_char in ['+', '-', " "]:
                if s_char == " ":
                    continue
                result_list.append(s_char)
            else:
                break

        if result_list:
            if result_list[0] == "-" and len(result_list) > 1:
                if int("".join(result_list[1:])) <= (1 << 31):
                    return int("".join(result_list))
                else:
                    return -(1 << 31)
            elif len(result_list) == 1 and (result_list[0] == "-" or result_list[0] == "+"):
                return 0
            else:
                if int("".join(result_list)) <= ((1 << 31) - 1):
                    return int("".join(result_list))
                else:
                    return (1 << 31) - 1


        else:
            return 0


# 正则表达式解法
import re
class Solution1:
    def myAtoi(self, s: str) -> int:
        matchs = re.match("^[\+\-]?\d+",s.lstrip())
        if not matchs:
            return 0
        return max(min(int(matchs.group(1)), 1<<31 -1), -1<<31)


# 状态机解法
INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31


class Automaton:
    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }

    def get_col(self, c):
        if c.isspace():
            return 0
        if c == '+' or c == '-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1


class Solution:
    def myAtoi(self, str: str) -> int:
        automaton = Automaton()
        for c in str:
            automaton.get(c)
        return automaton.sign * automaton.ans

