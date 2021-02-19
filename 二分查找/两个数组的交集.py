# -*- coding:utf-8 -*-
# @Time    : 2021/2/19 13:27
# @Author  : zengln
# @File    : 两个数组的交集.py

# 给定两个数组，编写一个函数来计算它们的交集。
#
#
#
#  示例 1：
#
#  输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2]
#
#
#  示例 2：
#
#  输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[9,4]
#
#
#
#  说明：
#
#
#  输出结果中的每个元素一定是唯一的。
#  我们可以不考虑输出结果的顺序。
#


# 哈希表解法
class Solution:
    def intersection(self, nums1, nums2):
        result_set = set()
        nums1_dict = {}
        for num in nums1:
            nums1_dict.setdefault(num, True)

        for num in nums2:
            if nums1_dict.get(num):
                result_set.add(num)

        return list(result_set)

# 双指针
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        tmp_nums1 = sorted(nums1)
        tmp_nums2 = sorted(nums2)
        nums1_index = 0
        nums2_index = 0
        result_set = set()
        while nums1_index != len(nums1) and nums2_index != len(nums2):
            if tmp_nums1[nums1_index] == tmp_nums2[nums2_index]:
                result_set.add(tmp_nums1[nums1_index])
                nums1_index += 1
                nums2_index += 1
            elif tmp_nums1[nums1_index] > tmp_nums2[nums2_index]:
                nums2_index += 1
            elif tmp_nums1[nums1_index] < tmp_nums2[nums2_index]:
                nums1_index += 1

        return list(result_set)

# 二分法
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        tmp_nums1 = sorted(nums1)
        tmp_nums2 = sorted(nums2)
        result_set = set()
        for num1 in tmp_nums1:
            left, right = 0, len(tmp_nums2) - 1
            while left <= right:
                mid = (left + right) // 2
                if tmp_nums2[mid] == num1:
                    result_set.add(num1)
                    break
                elif tmp_nums2[mid] > num1:
                    right = mid - 1
                elif tmp_nums2[mid] < num1:
                    left = mid + 1

        return list(result_set)