#!/usr/bin/python
"""You can see the description of the task using the code specified in the title on letcode.
This program have O(n) complexity by time and does not require additional memory

In this implementation I'm saving only last two fib numbers and based on them, I can calculate the next one
"""


class Solution:
    def fib(self, n):
        if n == 1 or n == 0:
            return n
        first, second = 0, 1
        for i in range(1, n):
            next = first + second
            first, second = second, next
        return next
