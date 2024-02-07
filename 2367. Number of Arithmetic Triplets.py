#!/usr/bin/python
"""You can see the description of the task using the code specified in the title on letcode.
As far as I understand, the worst case for time complexity is when all the elements are less than a given difference,
in this scenario we will have to check all the elements, then subtract 1 and go through them again, and again...
In the end we will make n passes, each of which will be by 1 shorter than the previous one.
It seems to me that the time complexity in this case will be equal to the sum of the arithmetic progression: n*n/2
which is O(n^2).
Also this program have O(n) complexity by space"""


class Solution:
    def arithmeticTriplets(self, nums, diff):
        self.glb_nums = nums
        self.glb_dif = diff
        self.border = len(nums)
        self.current_amount = 0

        for elem in range(self.border - 2):
            self.check(elem)
        return self.current_amount

    def check(self, pivot, shift=1, second=False):
        if pivot + shift < self.border:
            if self.glb_nums[pivot] + self.glb_dif == self.glb_nums[pivot + shift]:
                if not second:
                    return self.check(pivot=pivot + shift, shift=1, second=True)
                self.current_amount += 1
            elif self.glb_nums[pivot] + self.glb_dif > self.glb_nums[pivot + shift]:
                self.check(pivot=pivot, shift=shift+1, second=second)
