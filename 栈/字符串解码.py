# -*- coding:utf-8 -*-
# @Time    : 2020/7/15 9:17
# @Author  : zengln
# @File    : 字符串解码.py

# 给定一个经过编码的字符串，返回它解码后的字符串。
#
#  编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
#
#  你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
#
#  此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
#
#
#
#  示例 1：
#
#  输入：s = "3[a]2[bc]"
# 输出："aaabcbc"
#
#
#  示例 2：
#
#  输入：s = "3[a2[c]]"
# 输出："accaccacc"
#
#
#  示例 3：
#
#  输入：s = "2[abc]3[cd]ef"
# 输出："abcabccdcdcdef"
#
#
#  示例 4：
#
#  输入：s = "abc3[cd]xyz"
# 输出："abccdcdcdxyz"
#

'''
思路：
栈内数据格式: 次数[字符串]
遇到 ] 将上一个 [ 之内的字符串出栈,将字符串乘以出现次数后再入栈,
直到栈中无数据
无需重复字符, 直接在最终字符串后添加
'''
class Solution:
    def decodeString(self, s: str) -> str:
        result = ""
        stack = []
        num = ""
        for x in s:
            if x.isdigit():
               num += x
            elif x == "[":
                stack.append(int(num))
                num = ""
                stack.append(x)
            elif x == "]":
                tmp = stack.pop()
                tmp_list = []
                while tmp != "[":
                    tmp_list.append(tmp)
                    tmp = stack.pop()
                tmp_num = stack.pop()
                tmp_list = tmp_num * tmp_list
                if stack:
                    stack += tmp_list[::-1]
                else:
                    tmp_list = tmp_list
                    while tmp_list:
                        result += tmp_list.pop()
            elif stack:
                stack.append(x)
            elif not stack:
                result += x

        return result

'''
思路:
在栈中保存上一个字符串与当前字符串循环次数
结果 = 上一个字符串 + 当前字符串循环次数*当前字符串
'''
class Solution1:
    def decodeString(self, s: str) -> str:
        num = 0
        res = ""
        stack = []
        for x in s:
            if x.isdigit():
                num = num * 10 + int(x)
            elif x == "[":
                stack.append([num, res])
                res, num = "", 0
            elif x == "]":
                tmp_num, tmp_res = stack.pop()
                res = tmp_res + tmp_num * res
            else:
                res += x
        return res

'''
递归
'''
class Solution2:
    def decodeString(self, s: str) -> str:
        num = 0
        res = ""
        def help(s,index):
            while index < len(s):
                if '0' <= s[index] <= '9':
                    num = num * 10 + int(s[index])
                elif s[index] == '[':
                    tmp, index = help(s, index)
                    res = res + num * tmp
                    num = 0
                elif s[index] == ']':
                    return res, index
                else:
                    res += s[index]
                index += 1
            return res
        return res




s = Solution1()
print(s.decodeString("2[2[y]pq4[2[jk]e1[f]]]"))