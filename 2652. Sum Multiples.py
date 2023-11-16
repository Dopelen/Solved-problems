"""You can see the description of the task using the code specified in the title on letcode.
This program have O(n) complexity by time and does not require additional memory

Getting used to List Comprechantion
"""


class Solution:
    def sumOfMultiples(self, n):
        return sum([x for x in range(1, n + 1) if x % 3 == 0 or x % 5 == 0 or x % 7 == 0])
