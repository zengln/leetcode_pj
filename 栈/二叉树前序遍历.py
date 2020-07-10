# -*- coding:utf-8 -*-
# @Time    : 2020/7/10 9:38
# @Author  : zengln
# @File    : 二叉树前序遍历.py

# 给定一个二叉树，返回它的 前序 遍历。
#
#  示例:
#
#  输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# 输出: [1,2,3]
#
#
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List

# 栈
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if not root:
            return result

        stack = [root]
        while stack:
            root = stack.pop()
            result.append(root.val)
            if root.right:
                stack.append(root.right)

            if root.left:
                stack.append(root.left)
        return result


# 递归
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        def help(root, result):
            if not root:
                return result

            result.append(root.val)

            if root.left:
                help(root.left, result)

            if root.right:
                help(root.right, result)

            return result

        return help(root, result)