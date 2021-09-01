# -*- coding:utf-8 -*-
# @Time    : 2021/9/1 15:39
# @Author  : zengln
# @File    : 字母大小写全排列.py

# 给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。
#
#
#
#  示例：
# 输入：S = "a1b2"
# 输出：["a1b2", "a1B2", "A1b2", "A1B2"]
#
# 输入：S = "3z4"
# 输出：["3z4", "3Z4"]
#
# 输入：S = "12345"
# 输出：["12345"]
#
#
#
#
#  提示：
#
#
#  S 的长度不超过12。
#  S 仅由数字和字母组成。
#
#  Related Topics 位运算 字符串 回溯
#  👍 300 👎 0



class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def dfs(s, index, temp, result):
            if len(temp) == len(s):
                result.append(''.join(temp))
                return

            for i in range(index, len(s)):
                if len(temp) + len(s) - i != len(s):
                    continue

                if '0' <= s[i] <= '9':
                    temp.append(s[i])
                    dfs(s, i+1, temp, result)
                    temp.pop(-1)
                else:
                    # 小写递归一次
                    temp.append(s[i].lower())
                    dfs(s, i+1, temp, result)
                    temp.pop(-1)

                    # 大写递归一次
                    temp.append(s[i].upper())
                    dfs(s, i+1, temp, result)
                    temp.pop(-1)


        result = []
        temp = []
        dfs(s, 0, temp, result)
        return result
