class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        temp = head
        li = []
        index = 0
        while temp:
            li.append(temp.val)
            index += 1