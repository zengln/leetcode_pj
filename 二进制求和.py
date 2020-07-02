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


def addBinary(a:str, b:str) -> str:
    # return str(bin((int(a, 2) + int(b, 2))))[2:]
    # return bin((int(a, 2) + int(b, 2)))[2:]
    return '{0:b}'.format(int(a, 2) + int(b, 2))


a = "11"
b = "1"
print(addBinary(a, b))

