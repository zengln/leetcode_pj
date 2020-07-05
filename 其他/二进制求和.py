# -*- coding:utf-8 -*-
# @Time    : 2020/7/2 8:39
# @Author  : zengln
# @File    : 二进制求和.py

'''
给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。

示例一
输入: a = "11", b = "1"
输出: "100"

示例二
输入: a = "1010", b = "1011"
输出: "10101"
'''


def addBinary1(a:str, b:str) -> str:
    # return str(bin((int(a, 2) + int(b, 2))))[2:]
    # return bin((int(a, 2) + int(b, 2)))[2:]
    return '{0:b}'.format(int(a, 2) + int(b, 2))


def addBinary(a:str,b:str) -> str:
    if a.__len__() < b.__len__() :
        min_length = a.__len__()
    else:
        min_length = b.__len__()

    carry = 0
    num = ''

    # 按照最短的数据长度, 低位相加
    for i in range(min_length -1, -1, -1):
        sum = carry + int(a[i]) + int(b[i])
        num += str(sum % 2)
        carry = sum // 2

    # 如果 a 更长, a 继续进行运算
    if a.__len__() - min_length > 0:
        for i in range(0, a.__len__() - min_length):
            sum = carry + int(a[i])
            carry = sum // 2
            num += str(sum % 2)
    # 如果 b 更长, b 继续进行运算
    if b.__len__() - min_length > 0 :
        for i in range(0, b.__len__() - min_length):
            sum = carry + int(b[i])
            carry = sum // 2
            num += str(sum % 2)

    # 最终进位非0, 进1
    if carry == 1:
        num += '1'

    return ''.join(reversed(num))



a = "1010"
b = "1011"
print(addBinary(a, b))

