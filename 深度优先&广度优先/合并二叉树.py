# -*- coding:utf-8 -*-
# @Time    : 2021/8/30 11:44
# @Author  : zengln
# @File    : 合并二叉树.py

# 给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
#
#  你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点
# 。
#
#  示例 1:
#
#
# 输入:
# 	Tree 1                     Tree 2
#           1                         2
#          / \                       / \
#         3   2                     1   3
#        /                           \   \
#       5                             4   7
# 输出:
# 合并后的树:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \
# 	 5   4   7
#
#
#  注意: 合并必须从两个树的根节点开始。
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树
#  👍 755 👎 0



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    深度优先
    四种情况：
    当root1和root2 都有值：root1.val+root2.val 为新树的val，继续往下遍历root1和root2的左右节点
    当root1有值root2没值:新树当前节点等于root1，root2有root1无同理
    当root1和root2都没值: 新树当前也没值，直接返回None
    """
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        def dfs(root1, root2):
            tree = TreeNode()
            if not (root1 or root2):
                return None
            elif root1 and root2:
                tree.val = root1.val + root2.val
                tree.left = dfs(root1.left, root2.left)
                tree.right = dfs(root1.right, root2.right)
            elif root1:
                tree = root1
            elif root2:
                tree = root2
            return tree

        return dfs(root1, root2)

import collections
class Solution:

    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        t1 = root1
        t2 = root2
        if not t1:
            return t2
        if not t2:
            return t1

        merged = TreeNode(t1.val + t2.val)
        queue = collections.deque([merged])
        queue1 = collections.deque([t1])
        queue2 = collections.deque([t2])

        while queue1 and queue2:
            node = queue.popleft()
            node1 = queue1.popleft()
            node2 = queue2.popleft()
            left1, right1 = node1.left, node1.right
            left2, right2 = node2.left, node2.right
            if left1 or left2:
                if left1 and left2:
                    left = TreeNode(left1.val + left2.val)
                    node.left = left
                    queue.append(left)
                    queue1.append(left1)
                    queue2.append(left2)
                elif left1:
                    node.left = left1
                elif left2:
                    node.left = left2
            if right1 or right2:
                if right1 and right2:
                    right = TreeNode(right1.val + right2.val)
                    node.right = right
                    queue.append(right)
                    queue1.append(right1)
                    queue2.append(right2)
                elif right1:
                    node.right = right1
                elif right2:
                    node.right = right2
        return merged
