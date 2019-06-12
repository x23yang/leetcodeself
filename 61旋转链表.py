# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None or head.next == None:
            return head
        lengh = 0
        temp = head
        while temp:
            lengh += 1
            temp = temp.next
        k = k % lengh
        while k:
            temp = head
            while temp.next.next !=None:
                temp = temp.next
            last = temp.next
            last.next = head
            temp.next = None
            head = last
            k -= 1
        return head
if __name__ == '__main__':
    s=Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    temp = s.rotateRight(head,1)
    while temp :
        print(temp.val)
        temp = temp.next