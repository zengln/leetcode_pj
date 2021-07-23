# -*- coding:utf-8 -*-
# @Time    : 2021/7/23 17:29
# @Author  : zengln
# @File    : 判断子序列_动态规划.py

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




class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len, t_len = len(s), len(t)
        f = [[0] * 26 for _ in range(t_len)]

        """
        维护一个二维数组f[i][j], 在这个数组里
        横轴是a-z，26个字母
        纵轴是字符串t, 每一行对应的数据的意思是：
        假设选取一行, t字符串对应字母是s
        那么这一行的数据就是a-z这26个字母,
        在字符串t中s字母之后(包括当前位置)，出现的第一个位置。再也没出现设置为字母m 
        """
        f.append(['m'] * 26)
        for i in range(t_len-1, -1, -1):
            for j in range(26):
                f[i][j] = i if ord(t[i]) - ord('a') == j else f[i+1][j]
        '''
        上面的二维数组维护好后，遍历s字符串
        假设，当前s字符串对应的字符为a，这是第一个遍历的字符，a对应的列是0
        找 f[0](第一个字母所以从头开始找)[0](a在第0列)，
        如果f[0][0]为m：
        那么表示a在t[0]这个字母之后再也没有出现过,说明s不是t的子序列
        如果f[0][0]为1：
        那么标识a在t[0]这个字母后面第一次出现的位置为2,也就是说t[2]为a,
        说明a出现在2的位置，这时候就不需要再去关心1的位置是什么字母了。
        直接从f[3]开始遍历a的下一个字符。直到s全部遍历完毕或者遇到m
        '''
        count = 0
        for s_char in s:
            if f[count][ord(s_char) - ord('a')] == 'm':
                return False
            count = f[count][ord(s_char) - ord('a')] + 1

        return True

