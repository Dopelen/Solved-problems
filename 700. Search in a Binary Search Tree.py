"""You can see the description of the task using the code specified in the title on letcode.
This program have O(log(n)) complexity by time

This is realisation of basic binary tree operation, we are trying to find definite value in our tree.
The tree structure helps us discard half of the remaining search field after each program iteration,
allowing us to achieve O(log(n)) time. When the value is found we abort all remaining recursive operations.

ALSO, you can find simple and fast(if you are leetcode timer believer) iterative version of code right below.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    answer = None

    def searchBST(self, root, val):
        def check(self, root, val):
            if root == None or self.answer != None:
                return
            if root.val == val:
                self.answer = root
            elif root.val > val:
                return check(self, root.left, val)
            else:
                return check(self, root.right, val)

        check(self, root, val)
        return self.answer

# Iterative version
class Solution:
    def searchBST(self, root, val):
        while root != None:
            if root.val == val:
                break
            elif root.val > val:
                root = root.left
            else:
                root = root.right
        return root
