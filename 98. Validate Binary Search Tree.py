#!/usr/bin/python
"""You can see the description of the task using the code specified in the title on letcode.
This program have O(n) complexity by time

Oh... It was hard. You have to remember the definition of binary tree. The key of left/right SUBTREE (not Node)
have to be smaller/bigger, than key of subtree root. To comply with these conditions we must maintain boundaries.
This is achieved by maintaining the min and max.
For the left branches the limitation is - infinity, for the right ones + infinity,
difficulties arise when checking the right branches, inside the left ones (and symmetrically).
In this case, the key must be larger than the parent, but still remain smaller relative to all parent nodes.
This can be achieved by giving the child the upper limit that the parent has,
and the lower limit will be the value of the parent (for right branches inside the left branch)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root):
        def check(self, a, min, max):
            if a == None:
                return True
            if a.val <= min or max <= a.val:
                return False
            answer = check(self, a.left, min, a.val) and check(self, a.right, a.val, max)
            return answer
        return check(self, root, -math.inf, math.inf)
