# -*- coding:utf-8 -*-
# @Time    : 2020/7/8 19:41
# @Author  : zengln
# @File    : 二叉树的中序遍历.py

# 给定一个二叉树，返回它的中序 遍历。
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
# 输出: [1,3,2]
#
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        result = []

        def help(root, result):
            if root.left != None:
                help(root.left, result)

            result.append(root.val)

            if root.right != None:
                help(root.right, result)
            return result

        return help(root, result)


# 栈
class Solution1:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        result = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmp = stack.pop()
                result.append(tmp.val)
                root = tmp.right
        return result

# 栈
class Solution2:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        pass