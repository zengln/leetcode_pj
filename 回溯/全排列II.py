# -*- coding:utf-8 -*-
# @Time    : 2021/9/1 14:35
# @Author  : zengln
# @File    : 全排列II.py

# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
#
#
#
#  示例 1：
#
#
# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
#
#
#  示例 2：
#
#
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 8
#  -10 <= nums[i] <= 10
#
#  Related Topics 数组 回溯
#  👍 787 👎 0

from typing import List

class Solution:
    """
    在全排列的基础上，数组加上了可能存在相同值的情况，返回的结果中同样的结果要被排除掉

    在最后添加到结果集中先判断当前结果是否已经添加过，添加过直接忽略
    """
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, temp, use, result):
            if len(nums) == len(temp):
                if temp[:] not in result:
                    result.append(temp[:])
                return
            for i in range(len(nums)):
                if not use[i]:
                    use[i] = True
                    temp.append(nums[i])

                    dfs(nums, temp, use, result)

                    use[i] = False
                    temp.pop(-1)

        temp = []
        result = []
        use = [False for _ in range(len(nums))]
        dfs(nums, temp, use, result)
        return result

class Solution:
    """
    在递归的过程中去掉不需要的解
    """
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, temp, use, result):
            if len(nums) == len(temp):
                result.append(temp[:])
                return
            for i in range(len(nums)):
                if use[i]:
                    continue
                elif nums[i] == nums[i-1] and not use[i-1] and i > 0:
                    continue

                use[i] = True
                temp.append(nums[i])

                dfs(nums, temp, use, result)

                use[i] = False
                temp.pop(-1)

        temp = []
        result = []
        use = [False for _ in range(len(nums))]
        dfs(sorted(nums), temp, use, result)
        return result
