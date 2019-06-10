#迭代
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        res = None
        while head:
            node = ListNode(head.val)
            node.next =res 
            res = node
            head = head.next
        return res

if __name__=='__main__':
    s=Solution()
    head = ListNode(1)
    head.next =ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next =ListNode(4)

    temp = s.reverseList(head)
    while temp:
        print(temp.val)
        temp = temp.next 
