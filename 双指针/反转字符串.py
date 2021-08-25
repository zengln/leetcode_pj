# -*- coding:utf-8 -*-
# @Time    : 2021/8/25 19:12
# @Author  : zengln
# @File    : 反转字符串.py

# 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
#
#  不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
#
#  你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。
#
#
#
#  示例 1：
#
#  输入：["h","e","l","l","o"]
# 输出：["o","l","l","e","h"]
#
#
#  示例 2：
#
#  输入：["H","a","n","n","a","h"]
# 输出：["h","a","n","n","a","H"]
#  Related Topics 递归 双指针 字符串
#  👍 440 👎 0



class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        index_left = 0
        index_right = len(s) - 1
        while index_left < index_right:
            s[index_left], s[index_right] = s[index_right], s[index_left]
            index_left += 1
            index_right -= 1

