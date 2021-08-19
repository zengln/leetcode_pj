# -*- coding:utf-8 -*-
# @Time : 2021/8/19 23:21 
# @Author : zengln
# @File : 反转字符串中的元音字母.py 
# 给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。
#
#  元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现。
#
#
#
#  示例 1：
#
#
# 输入：s = "hello"
# 输出："holle"
#
#
#  示例 2：
#
#
# 输入：s = "leetcode"
# 输出："leotcede"
#
#
#
#  提示：
#
#
#  1 <= s.length <= 3 * 105
#  s 由 可打印的 ASCII 字符组成
#
#  Related Topics 双指针 字符串
#  👍 210 👎 0



class Solution:
    """
    两个指针从两头遍历，其中一个找到元音字母，则不动，直到另外一个找到元音字母，替换两者的位置，直到两个指针重合，退出循环
    """
    def reverseVowels(self, s: str) -> str:
        index_1 = 0
        index_2 = len(s) - 1
        ascii_list = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']

        while index_1 < index_2:
            if s[index_1] in ascii_list and s[index_2] in ascii_list:
                temp = s[:index_1] + s[index_2] + s[index_1+1:index_2] + s[index_1]
                if index_2 < len(s) - 1:
                    temp += s[index_2+1:]
                s = temp
                index_1 += 1
                index_2 -= 1
            elif s[index_1] in ascii_list:
                index_2 -= 1
            elif s[index_2] in ascii_list:
                index_1 += 1
            else:
                index_2 -= 1
                index_1 += 1
        return s


