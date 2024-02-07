#!/usr/bin/python
"""You can see the description of the task using the code specified in the title on letcode.
This program have O(n) complexity by time
The tricky part of this problem is "lexicographical order" in answer
So at the beginning I use List Comprehension to create "str" of numbers and sort it
Sorting will be lexicographical by default
For answer I convert str into int"""

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        answer = sorted([str(x) for x in range(1, n+1)])
        return list(map(int, answer))
