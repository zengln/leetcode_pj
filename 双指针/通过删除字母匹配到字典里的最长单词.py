# -*- coding:utf-8 -*-
# @Time : 2021/9/14 20:15 
# @Author : zengln
# @File : 通过删除字母匹配到字典里的最长单词.py 
# 给你一个字符串 s 和一个字符串数组 dictionary 作为字典，找出并返回字典中最长的字符串，该字符串可以通过删除 s 中的某些字符得到。
#
#  如果答案不止一个，返回长度最长且字典序最小的字符串。如果答案不存在，则返回空字符串。
#
#
#
#  示例 1：
#
#
# 输入：s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
# 输出："apple"
#
#
#  示例 2：
#
#
# 输入：s = "abpcplea", dictionary = ["a","b","c"]
# 输出："a"
#
#
#
#
#  提示：
#
#
#  1 <= s.length <= 1000
#  1 <= dictionary.length <= 1000
#  1 <= dictionary[i].length <= 1000
#  s 和 dictionary[i] 仅由小写英文字母组成
#
#  Related Topics 数组 双指针 字符串 排序

class Solution:
    """
    sort(key=lambda x:(-len(x), x) 设置两个排序键值
    """
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        result = ""
        dictionary.sort(key=lambda x: (-len(x), x))
        for temp_str in dictionary:
            index_s = 0
            index_t = 0
            while index_s < len(s) and index_t < len(temp_str):
                if s[index_s] == temp_str[index_t]:
                    index_t += 1

                index_s += 1
            if index_t == len(temp_str):
                result = temp_str
                break
        return result


