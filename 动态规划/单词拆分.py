# -*- coding:utf-8 -*-
# @Time : 2021/8/7 17:21 
# @Author : zengln
# @File : 单词拆分.py 
# 给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
#
#  说明：
#
#
#  拆分时可以重复使用字典中的单词。
#  你可以假设字典中没有重复的单词。
#
#
#  示例 1：
#
#  输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
#
#
#  示例 2：
#
#  输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
#      注意你可以重复使用字典中的单词。
#
#
#  示例 3：
#
#  输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false
#
#  Related Topics 字典树 记忆化搜索 哈希表 字符串 动态规划




class Solution:
    """
    暴力破解，直接遍历所有情况，确认是否有满足的情况
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        result = [False] * (len(s)+1)
        result[0] = True
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if result[i] and s[i:j] in wordDict:
                    result[j] = True
        return result[-1]



