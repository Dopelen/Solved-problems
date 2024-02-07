#!/usr/bin/python
"""You can see the description of the task using the code specified in the title on letcode.
This program have O(n) complexity by time

At the beginning we are finding all common elements in both lists
Then we add to answer the number of common elements, because this number will be the answer when we will stop checking lists
Next step - reverse both lists and iterate them in the same time using zip
If elem in "common" but was not found earlier, it means - now the time we have to increment number of common elements!
But we're moving backwards, so we decrease this number and then add him to "checked", so as not to do this again
At the end do not forget to delite last element (which we append at the beginning) and reverse the answer
"""

class Solution:
    def findThePrefixCommonArray(self, A, B):
        common = set(A) & set(B)
        common_el = len(common)
        if common_el == 0:
            return [0 * common_el]
        checked_elems = []
        answer = [common_el]
        A.reverse(), B.reverse()
        for x, y in zip(A,B):
            if x in common and x not in checked_elems:
                common_el -= 1
                checked_elems.append(x)
            if y in common and y not in checked_elems:
                common_el -= 1
                checked_elems.append(y)
            answer.append(common_el)
        answer.pop(), answer. reverse()
        return answer