# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return head
        lengh = 0
        temp = head
        while temp:
            lengh += 1
            temp = temp.next
        k = k % lengh
        if k ==0:
            return head
        cur = lengh
        temp = head
        while cur != k+1:
            cur -= 1
            temp = temp.next
        temp0 = temp.next
        start = temp.next
        temp.next = None
        while temp0.next:
            temp0 = temp0.next
        temp0.next = head
        head = start
        return head
if __name__ == '__main__':
    s=Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    temp = s.rotateRight(head,0)
    while temp :
        print(temp.val)
        temp = temp.next