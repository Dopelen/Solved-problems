"""You can see the description of the task using the code specified in the title on letcode.
This program have O(?) complexity by time


This is a straightforward solution. I create a dictionary with all possible digit squares to avoid repeated calculations.
Next, I divide number into digits and do the calculations, after which I save the resulting number into a dictionary with the passed values

There is another solution where you can avoid recording passed values by using only 2 pointers in Floyd/Brant algorithm
"""


class Solution:
    def isHappy(self, n):
        squares_of_numbers = {number: number ** 2 for number in range(0, 10)}
        passed_values = {}
        next_n = 0
        while n != 1:
            for digit in str(n):
                next_n += squares_of_numbers[int(digit)]
            if passed_values.get(next_n) != None:
                break
            passed_values[next_n] = True
            n, next_n = next_n, 0
        if n == 1:
            return True
        return False


A = Solution()
print(A.isHappy(19))
