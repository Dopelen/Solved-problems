"""You can see the description of the task using the code specified in the title on letcode.
This program have O(n) complexity by time
Here we fill hash-table with all symbols we have in "magazine"
And then we check if there are enough of them to create a “ransomeNote”.
"""


class Solution:
    def canConstruct(self, ransomNote, magazine):
        alphabet = {}
        for elem in magazine:
            if elem not in alphabet:
                alphabet[elem] = 1
            else:
                alphabet[elem] += 1
        for elem in ransomNote:
            if alphabet.get(elem) == None or alphabet[elem] == 0:
                return False
            else:
                alphabet[elem] -= 1
        return True