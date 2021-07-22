# -*- coding:utf-8 -*-
# @Time : 2021/7/22 6:56 
# @Author : zengln
# @File : 比特位计数.py 
# 给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
#
#  示例 1:
#
#  输入: 2
# 输出: [0,1,1]
#
#  示例 2:
#
#  输入: 5
# 输出: [0,1,1,2,1,2]
#
#  进阶:
#
#
#  给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
#  要求算法的空间复杂度为O(n)。
#  你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。
#
#  Related Topics 位运算 动态规划

# 用原生函数
class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n+1):
            temp = bin(i)
            result.append(temp.count('1'))
        return result


'''
奇偶找规律
奇数个数为上一个偶数的个数+1
偶数个数与除以2的偶数个数相等，除以2等于右移一位，去掉最后的0，1的个数不变
'''
class Solution2:
    def countBits(self, n: int) -> List[int]:
        result = [0]
        for i in range(1, n+1):
            if i % 2 == 0:
                result.append(result[i//2])
            else:
                result.append(result[i-1]+1)
        return result


"""
奇偶进阶写法
"""
class Solution5:
    def countBits(self, n: int) -> List[int]:
        bits = [0]
        for i in range(1, n + 1):
            bits.append(bits[i >> 1] + (i & 1))
        return bits

'''
知道之后会很轻松的知识：
x&(x-1)会将x最右边的一个1变为0
所以一直重复这个操作，直到x=0，统计重复了几次
就能算出x里1的个数
这个方法，不能算统计x里0的个数
'''
class Solution3:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n+1):
            result.append(self.fun(i))

        return result

    def fun(self, num):
        count = 0
        while num > 0:
            num &= (num-1)
            count += 1
        return count

