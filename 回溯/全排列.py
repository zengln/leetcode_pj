# -*- coding:utf-8 -*-
# @Time    : 2021/9/1 14:27
# @Author  : zengln
# @File    : 全排列.py

# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
#
#
#
#  示例 1：
#
#
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
#
#  示例 2：
#
#
# 输入：nums = [0,1]
# 输出：[[0,1],[1,0]]
#
#
#  示例 3：
#
#
# 输入：nums = [1]
# 输出：[[1]]
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 6
#  -10 <= nums[i] <= 10
#  nums 中的所有整数 互不相同
#
#  Related Topics 数组 回溯

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, use, temp, result):
            if len(temp) == len(nums):
                result.append(copy.deepcopy(temp))
                return

            for i in range(len(nums)):
                if not use[i]:
                    use[i] = True
                    temp.append(nums[i])

                    dfs(nums, use, temp, result)

                    use[i] = False
                    temp.pop(-1)

        result = []
        temp = []
        use = [False for _ in range(len(nums))]
        dfs(nums, use, temp, result)
        return result

