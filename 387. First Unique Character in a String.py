"""You can see the description of the task using the code specified in the title on letcode.
 This program have O(n) complexity by time
 The idea of solution is symple. We're just adding every character into hash-table with value : position,
 if symbol already in dict, then symbol's value becomes "None".
 After this we check one by one symbols in input, the first elem with "value : position" in our dict will be our answer """


class Solution:
    def firstUniqChar(self, s: str) -> int:
        all_char = {}
        step_counter = 0
        for elem in s:
            if elem in all_char:
                step_counter += 1
                all_char[elem] = None
                continue
            else:
                all_char[elem] = step_counter
                step_counter += 1
        for elem in s:
            if all_char[elem] != None:
                return all_char[elem]
        return -1
