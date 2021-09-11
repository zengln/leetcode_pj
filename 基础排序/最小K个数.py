# -*- coding:utf-8 -*-
# @Time    : 2021/9/3 9:00
# @Author  : zengln
# @File    : 最小K个数.py

# 设计一个算法，找出数组中最小的k个数。以任意顺序返回这k个数均可。
#
#  示例：
#
#  输入： arr = [1,3,5,7,2,4,6,8], k = 4
# 输出： [1,2,3,4]
#
#
#  提示：
#
#
#  0 <= len(arr) <= 100000
#  0 <= k <= min(100000, len(arr))
#
#  Related Topics 数组 分治 快速选择 排序 堆（优先队列）

class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        result = []
        for i in range(len(arr)):
            if i == 0:
                result.append(arr[i])
                continue
            left = 0
            right = len(result) - 1
            while left <= right:
                mid = (left + right) // 2
                if result[mid] > arr[i]:
                    right = mid - 1
                else:
                    left = mid + 1

            if left == 0:
                result.insert(0, arr[i])
            elif left == len(result):
                result.append(arr[i])
            else:
                result.insert(left, arr[i])

        return result[:k]

