"""You can see the description of the task using the code specified in the title on letcode.
This program have O(log(n)) complexity by time

Implementation of Iterative binary search algorithm
"""

class Solution:
    def search(self, nums, target):
        start = 0
        finish = len(nums)-1
        while start <= finish:
            midle = int(start + (finish - start) // 2)
            if target == nums[midle]:
                return midle
            elif nums[midle] > target:
                finish = midle - 1
            else:
                start = midle + 1
        return -1