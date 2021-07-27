# -*- coding:utf-8 -*-
# @Time    : 2021/7/27 16:51
# @Author  : zengln
# @File    : 除数博弈.py

# 爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。
#
#  最初，黑板上有一个数字 N 。在每个玩家的回合，玩家需要执行以下操作：
#
#
#  选出任一 x，满足 0 < x < N 且 N % x == 0 。
#  用 N - x 替换黑板上的数字 N 。
#
#
#  如果玩家无法执行这些操作，就会输掉游戏。
#
#  只有在爱丽丝在游戏中取得胜利时才返回 True，否则返回 False。假设两个玩家都以最佳状态参与游戏。
#
#
#
#
#
#
#  示例 1：
#
#  输入：2
# 输出：true
# 解释：爱丽丝选择 1，鲍勃无法进行操作。
#
#
#  示例 2：
#
#  输入：3
# 输出：false
# 解释：爱丽丝选择 1，鲍勃也选择 1，然后爱丽丝无法进行操作。
#
#
#
#
#  提示：
#
#
#  1 <= N <= 1000
#
#  Related Topics 脑筋急转弯 数学 动态规划 博弈

'''
每个数已经有确定的结果
后面的数字约数为比它小的数字，
算出比它小数字的结果，是输，那么当前数字一定会赢


思维盲点：想着一个数字需要多次计算，没想到数字有一个已经确定的结果
'''

class Solution:
    def divisorGame(self, n: int) -> bool:
        if n <= 1:
            return False

        result = [0] * (n+1)
        result[2] = 1
        for i in range(3, n+1):
            for j in range(1, i):
                if i % j == 0 and result[i-j] == 0:
                    result[i] = 1

        return result[n] == 1



"""
脑经急转弯
偶数必赢
奇数必输
"""
class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0