# -*- coding:utf-8 -*-
# @Time : 2021/7/23 6:53 
# @Author : zengln
# @File : 判断子序列.py 
# 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
#
#  字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"ae
# c"不是）。
#
#  进阶：
#
#  如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代
# 码？
#
#  致谢：
#
#  特别感谢 @pbrother 添加此问题并且创建所有测试用例。
#
#
#
#  示例 1：
#
#
# 输入：s = "abc", t = "ahbgdc"
# 输出：true
#
#
#  示例 2：
#
#
# 输入：s = "axc", t = "ahbgdc"
# 输出：false
#
#
#
#
#  提示：
#
#
#  0 <= s.length <= 100
#  0 <= t.length <= 10^4
#  两个字符串都只由小写字符组成。
#
#  Related Topics 双指针 字符串 动态规划

# 双指针
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index = 0
        t_index = 0

        if len(s) == 0:
            return True

        while (s_index < len(s)) and (t_index < len(t)):
            if s[s_index] == t[t_index]:
                s_index += 1

                if s_index == len(s):
                    return True
            t_index += 1

        return False

# 算是改进？
class Solution2:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        s_index = 0
        for t_char in t:
            if t_char != s[s_index]:
                continue
            s_index += 1
            if s_index == len(s):
                return True
        return False

# 又做一次，好像思路一样的
class Solution:
    """
    s[0:i]如果为t的子序列, 那么s[0:i-1]必定是t的子序列
    所以
    dp[i] = dp[i-1] and (s[i] == t[j])
    """
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        result = [False] * len(s)
        index_t = 0
        index_s = 0
        while index_t < len(t) and index_s < len(s):
            if s[index_s] == t[index_t]:
                result[index_s] = True
                index_s += 1
            index_t += 1
        return result[-1]


class Solution:
    """
    动态规划思路：
    使用一个二维数组表示dp[i][j]表示i位置后第一次出现字符j的位置
    后续判断子序列，就通过这个二维数组判断
    """

    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        result = [[-1] * 26 for _ in range(len(t) + 1)]

        for i in range(len(t) - 1, -1, -1):
            for j in range(26):
                if ord(t[i]) == ord('a') + j:
                    result[i][j] = i
                else:
                    result[i][j] = result[i + 1][j]

        index = 0
        for s_chr in s:
            temp = ord(s_chr) - ord('a')
            if result[index][temp] == -1:
                return False
            index = result[index][temp] + 1
        return True