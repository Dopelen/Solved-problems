"""You can see the description of the task using the code specified in the title on letcode.
This program have O(n) complexity by time

Here I have plural answer for easy problem"""


# O(n^2) time, O(n) space
class Solution:
    def runningSum(self, nums):
        our_list = list(nums)
        lenght = len(our_list)
        complited_answer = [sum(our_list[:i]) for i in range(1, lenght + 1)]
        return complited_answer


# O(n^2) time, O(n) space. Same but List Comrehantion
class Solution:
    def runningSum(self, nums):
        return [sum(list(nums)[:i]) for i in range(1, len(list(nums)) + 1)]


# O(n) time, O(1) space
class Solution:
    def runningSum(self, nums):
        our_list = list(nums)
        for i in range(1, len(our_list)):
            our_list[i] = our_list[i - 1] + our_list[i]
        return our_list
