# -*- coding:utf-8 -*-
# @Time    : 2021/8/12 16:27
# @Author  : zengln
# @File    : 矩阵区域和.py

# 给你一个 m x n 的矩阵 mat 和一个整数 k ，请你返回一个矩阵 answer ，其中每个 answer[i][j] 是所有满足下述条件的元素 ma
# t[r][c] 的和：
#
#
#  i - k <= r <= i + k,
#  j - k <= c <= j + k 且
#  (r, c) 在矩阵内。
#
#
#
#
#  示例 1：
#
#
# 输入：mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
# 输出：[[12,21,16],[27,45,33],[24,39,28]]
#
#
#  示例 2：
#
#
# 输入：mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
# 输出：[[45,45,45],[45,45,45],[45,45,45]]
#
#
#
#
#  提示：
#
#
#  m == mat.length
#  n == mat[i].length
#  1 <= m, n, k <= 100
#  1 <= mat[i][j] <= 100
#
#  Related Topics 数组 矩阵 前缀和
#  👍 92 👎 0

# 暴力破解，时间复杂度 N的四次方
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        result = []
        for i in range(len(mat)):
            temp = list()
            for j in range(len(mat[i])):
                temp.append(0)
                for index_i in range(max(i-k, 0), min(i+k, len(mat)-1)+1, 1):
                    for index_j in range(max(j-k, 0), min(j+k, len(mat[i])-1)+1, 1):
                        temp[-1] += mat[index_i][index_j]
            result.append(temp)
        return result


# 改进，时间复杂度N的平方
class Solution:
    """
    使用一个二维数组mat_sum，保存从左上角(0,0)到当前位置 mat[i][j]的和
    例如i=1,j=1,那么
    mat_sum[i][1] = mat[0][0]+mat[0][1]+mat[1][0]+mat[1][1]

    那么提意需要计算的某个和一定小于等于mat_sum[i][j]
    如果小于：
    result[i][j] = mat_sum[i+k][j+k] + mat_sum[i-k-1][j-k-1] - mat_sum[i-k-1][j+k] - mat_sum[i+k][j-k-1]
    """
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        mat_sum = []
        for i in range(len(mat)):
            mat_sum.append([0] * len(mat[i]))
            mat_sum[i][0] = mat_sum[i-1][0] + mat[i][0]
            for j in range(len(mat[i])):
                if i == 0 and j == 0:
                    mat_sum[0][0] = mat[0][0]
                elif i == 0:
                    mat_sum[i][j] = mat_sum[i][j-1] + mat[i][j]
                elif j == 0:
                    mat_sum[i][j] = mat_sum[i-1][j] + mat[i][j]
                else:
                    mat_sum[i][j] = mat_sum[i-1][j] + mat_sum[i][j-1] - mat_sum[i-1][j-1] + mat[i][j]
        print(mat_sum)
        result = []
        for i in range(len(mat)):
            result.append(list())

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i - k <= 0 and j - k <= 0:
                    temp = mat_sum[min(i+k, len(mat)-1)][min(j+k, len(mat[i])-1)]
                elif i - k > 0 and j - k <= 0:
                    temp = mat_sum[min(i+k, len(mat)-1)][min(j+k, len(mat[i])-1)] - mat_sum[i-k-1][min(j+k, len(mat[i])-1)]
                elif i - k <= 0 and j - k > 0:
                    temp = mat_sum[min(i+k, len(mat)-1)][min(j+k, len(mat[i])-1)] - mat_sum[min(i+k, len(mat)-1)][j-k-1]
                else:
                    temp = mat_sum[min(i+k, len(mat)-1)][min(j+k, len(mat[i])-1)] - mat_sum[min(i+k, len(mat)-1)][j-k-1] - mat_sum[i-k-1][min(j+k, len(mat[i])-1)] + mat_sum[i-k-1][j-k-1]
                result[i].append(temp)
        return result