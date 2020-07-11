# 实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。
#
#  调用 next() 将返回二叉搜索树中的下一个最小的数。
#
#
#
#  示例：
#
#
#
#  BSTIterator iterator = new BSTIterator(root);
# iterator.next();    // 返回 3
# iterator.next();    // 返回 7
# iterator.hasNext(); // 返回 true
# iterator.next();    // 返回 9
# iterator.hasNext(); // 返回 true
# iterator.next();    // 返回 15
# iterator.hasNext(); // 返回 true
# iterator.next();    // 返回 20
# iterator.hasNext(); // 返回 false
#
#
#
#  提示：
#
#
#  next() 和 hasNext() 操作的时间复杂度是 O(1)，并使用 O(h) 内存，其中 h 是树的高度。
#  你可以假设 next() 调用总是有效的，也就是说，当调用 next() 时，BST 中至少存在一个下一个最小的数。
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:

    # def __init__(self, root: TreeNode):
    #     self.result = []
    #     if root:
    #         stack = [root]
    #         flag = False
    #         while stack:
    #             tmp = stack.pop()
    #             if tmp == flag:
    #                 self.result.append(stack.pop().val)
    #             else:
    #                 if tmp.right:
    #                     stack.append(tmp.right)
    #                 if tmp.left:
    #                     stack.append(tmp.left)
    #                 stack.append(tmp)
    #                 stack.append(flag)
    #         self.result.sort(reverse=True)

    # 二叉搜索树为特殊二叉树, 左节点恒比根节点小, 右节点恒比根节点大,使用中序遍历可得从小到大排序数组
    def __init__(self, root: TreeNode):
        self.result = []
        if root:
            stack = [root]
            flag = False
            while stack:
                tmp = stack.pop()
                if tmp == flag:
                    self.result.append(stack.pop().val)
                else:
                    if tmp.right:
                        stack.append(tmp.right)
                    stack.append(tmp)
                    stack.append(flag)
                    if tmp.left:
                        stack.append(tmp.left)
            self.result = self.result[::-1]

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.result.pop()


    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.result:
            return True
        else:
            return False



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

