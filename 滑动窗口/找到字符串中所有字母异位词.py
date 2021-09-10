# -*- coding:utf-8 -*-
# @Time    : 2021/9/10 16:10
# @Author  : zengln
# @File    : 找到字符串中所有字母异位词.py

# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
#
#  异位词 指字母相同，但排列不同的字符串。
#
#
#
#  示例 1:
#
#
# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0,6]
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
#
#
#  示例 2:
#
#
# 输入: s = "abab", p = "ab"
# 输出: [0,1,2]
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
#
#
#
#
#  提示:
#
#
#  1 <= s.length, p.length <= 3 * 104
#  s 和 p 仅包含小写字母
#
#  Related Topics 哈希表 字符串 滑动窗口
#  👍 608 👎 0


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        result = []
        count_p = [0] * 26
        count_s = [0] * 26
        for index in range(len(p)):
            count_p[ord(p[index]) - ord('a')] += 1
            count_s[ord(s[index]) - ord('a')] += 1

        if count_s == count_p:
            result.append(0)

        for i in range(len(p), len(s)):
            count_s[ord(s[i-len(p)]) - ord('a')] -= 1
            count_s[ord(s[i]) - ord('a')] += 1
            if count_s == count_p:
                result.append(i + 1 - len(p))

        return result



