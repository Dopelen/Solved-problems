#!/usr/bin/python
"""You can see the description of the task using the code specified in the title on letcode.
This program have O(n) complexity by time

Surprisingly simple exercise without hidden pain.
The only thing that made me think about, what is faster is to compare two numbers using ">" and "<" or to subtract them?
I started trying to find the answer using timeit(), which showed that in general they have the same execution time"""


class Solution:
    def busyStudent(self, startTime, endTime, queryTime):
        answer = 0
        iterations = len(startTime)
        for step in range(iterations):
            if startTime[step] <= queryTime and endTime[step] >= queryTime:
                answer += 1
        return answer
