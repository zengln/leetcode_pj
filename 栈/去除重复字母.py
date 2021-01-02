# 给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。
#
#  注意：该题与 1081 https://leetcode-cn.com/problems/smallest-subsequence-of-distinct
# -characters 相同
#
#
#
#  示例 1：
#
#
# 输入：s = "bcabc"
# 输出："abc"
#
#
#  示例 2：
#
#
# 输入：s = "cbacdcbc"
# 输出："acdb"
#
#
#
#  提示：
#
#
#  1 <= s.length <= 104
#  s 由小写英文字母组成
#


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack_char = []
        for index_s in range(len(s)):
            char = s[index_s]
            num = len(stack_char)
            for index in range(num):
                if stack_char[-1] > char and stack_char[-1] in s[index_s+1:len(s)] and char not in stack_char:
                    stack_char.pop()

            if char not in stack_char:
                stack_char.append(char)
        return ''.join(stack_char)


