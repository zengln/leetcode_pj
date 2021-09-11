# -*- coding:utf-8 -*-
# @Time    : 2021/9/6 19:36
# @Author  : zengln
# @File    : 搜索二维矩阵.py

# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
#
#
#  每行中的整数从左到右按升序排列。
#  每行的第一个整数大于前一行的最后一个整数。
#
#
#
#
#  示例 1：
#
#
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# 输出：true
#
#
#  示例 2：
#
#
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# 输出：false
#
#
#
#
#  提示：
#
#
#  m == matrix.length
#  n == matrix[i].length
#  1 <= m, n <= 100
#  -104 <= matrix[i][j], target <= 104
#
#  Related Topics 数组 二分查找 矩阵
#  👍 500 👎 0



class Solution:
    """
    先确定在哪一行, 再在那一行找
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        left = 0
        right = len(matrix) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid

        if matrix[left][-1] < target:
            return False

        temp = left
        right = len(matrix[0]) - 1
        left = 0
        while left <= right:
            mid = (left + right) // 2
            if matrix[temp][mid] == target:
                return True
            elif matrix[temp][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False


