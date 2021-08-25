# -*- coding:utf-8 -*-
# @Time    : 2021/8/25 19:29
# @Author  : zengln
# @File    : 反转字符串中的单词 III.py

# 给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
#
#
#
#  示例：
#
#  输入："Let's take LeetCode contest"
# 输出："s'teL ekat edoCteeL tsetnoc"
#
#
#
#
#  提示：
#
#
#  在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。
#
#  Related Topics 双指针 字符串
#  👍 318 👎 0



class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split(" ")
        for index in range(len(s_list)):
            s_list[index] = s_list[index][::-1]
        return ' '.join(s_list)

