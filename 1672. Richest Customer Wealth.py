#!/usr/bin/python
"""You can see the description of the task using the code specified in the title on letcode.
This program have O(n) complexity by time

Check every costumer, if his budged > last biggest, than change last biggest"""


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        customers, richest_budget = len(accounts), sum(accounts[0])
        for person in range(1, customers):
            budget = sum(accounts[person])
            if budget > richest_budget:
                richest_budget = budget
        return richest_budget
