# -*- coding:utf-8 -*-
# @Time    : 2021/8/27 19:49
# @Author  : zengln
# @File    : 字符串的排列.py

# 给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。
#
#  换句话说，s1 的排列之一是 s2 的 子串 。
#
#
#
#  示例 1：
#
#
# 输入：s1 = "ab" s2 = "eidbaooo"
# 输出：true
# 解释：s2 包含 s1 的排列之一 ("ba").
#
#
#  示例 2：
#
#
# 输入：s1= "ab" s2 = "eidboaoo"
# 输出：false
#
#
#
#
#  提示：
#
#
#  1 <= s1.length, s2.length <= 104
#  s1 和 s2 仅包含小写字母
#
#  Related Topics 哈希表 双指针 字符串 滑动窗口
#  👍 421 👎 0



class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_count = [0] * 26
        s2_count = [0] * 26
        for i in range(len(s1)):
            s1_count[ord(s1[i])-ord('a')] += 1
            s2_count[ord(s2[i])-ord('a')] += 1

        if s1_count == s2_count:
            return True

        for i in range(len(s1), len(s2)):
            s2_count[ord(s2[i-len(s1)])-ord('a')] -= 1
            s2_count[ord(s2[i])-ord('a')] += 1

            if s1_count == s2_count:
                return True

        return False




