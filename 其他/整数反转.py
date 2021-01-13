# -*- coding:utf-8 -*-
# @Time    : 2021/1/12 20:33
# @Author  : zengln
# @File    : 整数反转.py

# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
#
#
#
#  注意：
#
#
#  假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231, 231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
#
#
#
#
#  示例 1：
#
#
# 输入：x = 123
# 输出：321
#
#
#  示例 2：
#
#
# 输入：x = -123
# 输出：-321
#
#
#  示例 3：
#
#
# 输入：x = 120
# 输出：21
#
#
#  示例 4：
#
#
# 输入：x = 0
# 输出：0
#
#
#
#
#  提示：
#
#
#  -231 <= x <= 231 - 1
#

class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)
        result = 0
        if x_str[0] == "-":
            x_str = x_str[::-1][:-1]
            if int("".join(x_str)) <= 2 ** 31:
                 result = 0 - int("".join(x_str))

        else:
            x_str = x_str[::-1]
            if int("".join(x_str)) <= 2 ** 31 - 1:
                result = int("".join(x_str))

        return result

'''
大佬解法
51.47%
9.02%
直接使用整数
        x_abs = abs(x)
        result = 0

        max_number = (1 << 31) - 1 if x > 0 else 1 << 31
        while x_abs != 0:
            result = result * 10 + x_abs % 10
            if result > max_number:
                return 0
            x_abs = x_abs // 10

        return result if x > 0 else - result
'''

