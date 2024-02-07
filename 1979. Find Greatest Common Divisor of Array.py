#!/usr/bin/python
"""You can see the description of the task using the code specified in the title on letcode.
This program have O(n) complexity by time and does not require additional memory

Finding min and max by using built-in functions and then use Euclid's theorem to find the greatest common divisor
"""

class Solution:
    def findGCD(self, nums):
        a, b = max(nums), min(nums)
        if a == b:
            return a
        while b != 0:
            a = a%b
            a, b = b, a
        return a