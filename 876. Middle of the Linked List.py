"""You can see the description of the task using the code specified in the title on letcode.
This program have O(n) complexity by time
"next" here is the function defined in a Class by condition
Since the structure used here is a linked list I just go through all list and count elements then
I divide number of elements by 2 and go backward this amount of steps

Alternative and more "advanced" solution is go front to back and back to front until pointers didn't meet
"""


class Solution:
    def middleNode(self, head):
        counter = 0
        temp = head
        while temp:
            counter += 1
            temp = temp.next
        temp = head
        for i in range(counter // 2):
            temp = temp.next
        return temp
