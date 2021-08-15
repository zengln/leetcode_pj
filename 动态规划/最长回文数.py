# -*- coding:utf-8 -*-
# @Time : 2021/8/15 12:05 
# @Author : zengln
# @File : 最长回文数.py 
# 给你一个字符串 s，找到 s 中最长的回文子串。
#
#
#
#  示例 1：
#
#
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
#
#
#  示例 2：
#
#
# 输入：s = "cbbd"
# 输出："bb"
#
#
#  示例 3：
#
#
# 输入：s = "a"
# 输出："a"
#
#
#  示例 4：
#
#
# 输入：s = "ac"
# 输出："a"
#
#
#
#
#  提示：
#
#
#  1 <= s.length <= 1000
#  s 仅由数字和英文字母（大写和/或小写）组成
#
#  Related Topics 字符串 动态规划
#  👍 3958 👎 0



class Solution:
    """
    超时了
    以当前位置为结束,找到当前位置最长回文子串
    回文子串, 第一个字符与最后一个字符必定相同，使用一个字典，key为字符，value为保存当前位置出现位置的list，
    字段中没有则回文字串长度为1
    字段中有则依次从最前面的位置开始判断，是否为回文字串，是则与已经找到的最长回文字串判断长度
    """
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(s, start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        char_index = dict()
        result = ""
        for i in range(len(s)):
            index_list = char_index.get(s[i], None)
            if not index_list:
                char_index.setdefault(s[i], []).append(i)
                if len(result) < len(s[i]):
                    result = s[i]
                continue

            for index in index_list:
                if isPalindrome(s, index, i):
                    if len(result) < (i - index + 1):
                        result = s[index:i+1]
                        break
            char_index[s[i]].append(i)
        return result


class Solution:
    """
    用一个二维数组保存, 保存所有字串是否为回文串的结果,找到其中最长的回文串
    假设dp[i][j]表示S以i开头,j结尾的一个字串,
    如果dp[i+1][j-1]为回文串且s[i]==s[j]那么dp[i][j]则为回文串
    dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
    """
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        begin = 0
        end = 0
        dp = [[False] * n for _ in range(n)]
        for j in range(n):
            for i in range(n):
                if j < i:
                    continue
                if i == j:
                    dp[i][j] = True
                    continue

                if s[i] == s[j] and (dp[i+1][j-1] or j - i == 1):
                    dp[i][j] = True
                    if j - i > end - begin:
                        begin = i
                        end = j
        # print(dp)
        return s[begin: end+1]

