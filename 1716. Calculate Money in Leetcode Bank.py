"""You can see the description of the task using the code specified in the title on letcode.
This program have O(1) complexity by time

The idea is simple: just use the arithmetic progression formula plural times! To calculate the increase for each week (“bonus”)
and then calculate the value of the remainder.
I like this task
"""

class Solution:
    def totalMoney(self, n):
        formula = int((1 + n) * n / 2)
        if n <= 7:
            return formula
        weeks, leftovers = n // 7, n % 7
        main = int(28 * weeks)
        bonus = int((7 * weeks * (weeks - 1)) / 2)
        leftovers = int(((weeks + 1) + (weeks + leftovers)) * leftovers / 2)
        return main + bonus + leftovers