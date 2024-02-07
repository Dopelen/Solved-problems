#!/usr/bin/python
"""You can see the description of the task using the code specified in the title on letcode.
This program have O(1) complexity by time

Check equality, return response"""


class Solution:
    def checkTree(self, root):
        if root.val == root.left.val + root.right.val:
            return True
        return False