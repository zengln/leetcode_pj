# -*- coding:utf-8 -*-
# @Time    : 2021/9/1 15:12
# @Author  : zengln
# @File    : 组合.py

# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
#
#  你可以按 任何顺序 返回答案。
#
#
#
#  示例 1：
#
#
# 输入：n = 4, k = 2
# 输出：
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
#
#  示例 2：
#
#
# 输入：n = 1, k = 1
# 输出：[[1]]
#
#
#
#  提示：
#
#
#  1 <= n <= 20
#  1 <= k <= n
#
#  Related Topics 数组 回溯

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(index, temp, result):
            if len(temp) == k:
                result.append(temp[:])
            for i in range(index, n+1):
                temp.append(i)
                dfs(i+1, temp, result)
                temp.pop(-1)

        result = []
        temp = []
        dfs(1, temp, result)
        return result

