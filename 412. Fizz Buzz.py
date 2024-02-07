#!/usr/bin/python
"""You can see the description of the task using the code specified in the title on letcode.
This program have O(n) complexity by time

The solution of classic problem by using List Comprehension"""

class Solution:
    def fizzBuzz(self, n: int):
        return ["FizzBuzz" if x%3 == 0 and x%5 == 0 else "Fizz" if x%3 == 0 else "Buzz" if x%5 == 0 else str(x) for x in range(1, n+1)]
