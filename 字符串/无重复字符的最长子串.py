# -*- coding:utf-8 -*-
# @Time    : 2021/8/27 15:56
# @Author  : zengln
# @File    : 无重复字符的最长子串.py

# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
#
#
#
#  示例 1:
#
#
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#
#
#  示例 2:
#
#
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#
#
#  示例 3:
#
#
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#
#
#  示例 4:
#
#
# 输入: s = ""
# 输出: 0
#
#
#
#
#  提示：
#
#
#  0 <= s.length <= 5 * 104
#  s 由英文字母、数字、符号和空格组成
#
#  Related Topics 哈希表 字符串 滑动窗口
#  👍 6004 👎 0



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        index = 0
        temp = list()
        while index < len(s):
            if s[index] in temp:
                result = max(result, len(temp))

                temp_index = temp.index(s[index])
                temp = temp[temp_index+1:]

            temp.append(s[index])
            index += 1
        return max(result, len(temp))



