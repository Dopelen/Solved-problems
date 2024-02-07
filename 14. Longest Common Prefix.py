#!/usr/bin/python
"""You can see the description of the task using the code specified in the title on letcode.
This program have O(n * m) complexity by time, where "n" the number of words in input and "m" size of the smallest word

I personally like this problem and mine solution, simple and cool

"""


class Solution:
    def longestCommonPrefix(self, strs):
        min_len = 201

        for elem in strs:
            if len(elem) < min_len:
                min_len = len(elem)

        for step in range(min_len):
            pivot = strs[0][step]
            for element in strs:
                if element[step] != pivot:
                    return strs[0][0:step]

        return strs[0][0:min_len]