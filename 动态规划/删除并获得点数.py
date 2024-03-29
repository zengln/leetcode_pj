# -*- coding:utf-8 -*-
# @Time : 2021/8/1 13:56 
# @Author : zengln
# @File : 删除并获得点数.py 
# 给你一个整数数组 nums ，你可以对它进行一些操作。
#
#  每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除 所有 等于 nums[i] - 1 和 nums[i]
#  + 1 的元素。
#
#  开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。
#
#
#
#  示例 1：
#
#
# 输入：nums = [3,4,2]
# 输出：6
# 解释：
# 删除 4 获得 4 个点数，因此 3 也被删除。
# 之后，删除 2 获得 2 个点数。总共获得 6 个点数。
#
#
#  示例 2：
#
#
# 输入：nums = [2,2,3,3,3,4]
# 输出：9
# 解释：
# 删除 3 获得 3 个点数，接着要删除两个 2 和 4 。
# 之后，再次删除 3 获得 3 个点数，再次删除 3 获得 3 个点数。
# 总共获得 9 个点数。
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 2 * 104
#  1 <= nums[i] <= 104
#
#  Related Topics 数组 哈希表 动态规划




class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # 将每个数出现的次数统计出来，次数X数=删除这个数获取的最大积分
        # 将最大积分按照数的大小排序，算出能获取到的最大积分
        # 思维盲点在于，动态规划的数组是自己构造的，不是题目直接给出的
        # 在N点，获取的最大点数max(N-1, N-2的点数+ N的点数)
        # 打家劫舍变种题
        max_value = max(nums)
        result = [0] * (max_value + 1)
        for i in nums:
            result[i] += i

        max_result = max(result[0], result[1])
        a = result[0]
        b = result[1]
        for i in range(2, len(result)):
            max_result = max(b, a+result[i])
            a, b = b, max_result
        return max_result

