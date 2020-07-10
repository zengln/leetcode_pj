# -*- coding:utf-8 -*-
# @Time    : 2020/7/10 15:07
# @Author  : zengln
# @File    : 二叉树的锯齿形层次遍历.py

# 给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
#
#  例如：
# 给定二叉树 [3,9,20,null,null,15,7],
#
#      3
#    / \
#   9  20
#     /  \
#    15   7
#
#
#  返回锯齿形层次遍历如下：
#
#  [
#   [3],
#   [20,9],
#   [15,7]
# ]
#

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if not root:
            return result

        stack1 = [root]
        stack2 = []
        tmp_result = []
        flag = False
        while stack1:
            tmp = stack1.pop()
            tmp_result.append(tmp.val)
            if flag:
                if tmp.left:
                    stack2.append(tmp.left)

                if tmp.right:
                    stack2.append(tmp.right)
            else:
                if tmp.right:
                    stack2.append(tmp.right)

                if tmp.left:
                    stack2.append(tmp.left)

            if not stack1:
                result.append(tmp_result)
                tmp_result = []
                while stack2:
                    stack1.append(stack2.pop())
                flag = bool(1 - flag)
        return result


