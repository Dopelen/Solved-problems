"""You can see the description of the task using the code specified in the title on letcode.
This program have O(n) complexity by time and some depth of the recursion

Here I have plural answer for easy problem"""


class Solution:
    def invertTree(self, root):
        if root:
            root.left, root.right = root.right, root.left
            Solution.invertTree(self, root.left)
            Solution.invertTree(self, root.right)
        return (root)
