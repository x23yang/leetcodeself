# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        if head ==None or head.next ==None:
            return  head
        res = self.reverseList(head.next)
        t = head.next
        head.next = None
        t.next = head
        return res
if __name__=='__main__':
    s=Solution()
    head = ListNode(1)
    head.next=ListNode(2)
    head.next.next = ListNode(3)
    temp = s.reverseList(head)
    while temp:
        print(temp.val)
        temp = temp.next
