# -*- coding:utf-8 -*-
# @Time : 2021/8/7 17:53 
# @Author : zengln
# @File : 接雨水.py 
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
#
#
#  示例 1：
#
#
#
#
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
#
#
#  示例 2：
#
#
# 输入：height = [4,2,0,3,2,5]
# 输出：9
#
#
#
#
#  提示：
#
#
#  n == height.length
#  0 <= n <= 3 * 104
#  0 <= height[i] <= 105
#
#  Related Topics 栈 数组 双指针 动态规划 单调栈

class Solution:
    """
    每个点能接到的雨水为其左右两边中的低一点的高度-当前高度
    有当前节点i，保存的雨水为
    dp[i] = min(right_height, left_height) - height[i]
    所以需要两个数组保存当前节点，左右两边最大高度
    """
    def trap(self, height: List[int]) -> int:
        height_len = len(height)
        height_right = [0] * height_len
        height_left = [0] * height_len
        result = [0] * height_len
        for i in range(1, height_len):
            height_left[i] = height[i-1] if height[i-1] > height_left[i-1] else height_left[i-1]

        for i in range(height_len-2, -1, -1):
            height_right[i] = height[i+1] if height[i+1] > height_right[i+1] else height_right[i+1]

        for i in range(height_len):
            temp = min(height_right[i], height_left[i]) - height[i]
            if temp <= 0:
                result[i] = 0
            else:
                result[i] = temp
        return sum(result)

