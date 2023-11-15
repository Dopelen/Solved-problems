"""You can see the description of the task using the code specified in the title on letcode.
This program have O(log(n)) complexity by time

This problem has the straight forward solution, where you simply combine subtraction and division
depending on whether the number is even or not.
My solution does the same thing, except that if the number is a power of two, we can immediately print the solution,
which can speed up our code. For the same reason I use bitwise division by 2 """

class Solution:
    def numberOfSteps(self, num):
        counter = 0
        while num != 0:
            if (num & (num-1) == 0):
                return counter + int(len(bin(num)) - bin(num).find("1"))
            elif not (num & 1):
                num = num >> 1
            else:
                num = num - 1
            counter += 1
        return counter