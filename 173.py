from typing import List
import sys


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.push_stack(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        cur_node = self.stack.pop()
        if cur_node.right:
            self.push_stack(cur_node.right)
        return cur_node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.stack:
            return True
        return False

    def push_stack(self, node: TreeNode):
        while node:
            self.stack.append(node)
            node = node.left




