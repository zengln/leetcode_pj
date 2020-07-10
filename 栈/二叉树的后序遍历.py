# -*- coding:utf-8 -*-
# @Time    : 2020/7/10 14:06
# @Author  : zengln
# @File    : 二叉树的后序遍历.py

# 给定一个二叉树，返回它的 后序 遍历。
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
# 输出: [3,2,1]
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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if not root:
            return result

        stack = [root]

        # 标识是否二次进栈
        flag = False

        while stack:
            tmp = stack.pop()
            if tmp != flag:
                stack.append(tmp)
                stack.append(flag)
                if tmp.right:
                    stack.append(tmp.right)
                if tmp.left:
                    stack.append(tmp.left)
            else:
                result.append(stack.pop().val)
        return result

# 递归
class Solution1:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        def help(root, result):
            if not root:
                return result

            if root.left:
                help(root.left, result)

            if root.right:
                help(root.right, result)

            result.append(root.val)
            return result

        return help(root, result)