class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a=[]
        b=[]
        while l1 :
            a.append(l1.val)
            l1 = l1.next
        while l2 :
            b.append(l2.val)
            l2 = l2.next
        a.reverse()
        a=map(lambda x :str(x),a)
        a=''.join(a)
        b.reverse()
        b = map(lambda x: str(x), b)
        b = ''.join(b)
        if a == '':
            a = 0
        else:
            a = int(a)
        if b == '':
            b = 0
        else:
            b=int(b)
        c=a+b
        c=str(c)
        head = ListNode(c[0])
        for i in range(1,len(c)):
            node = ListNode(c[i])
            node.next = head
            head = node
        return head
if __name__ == '__main__':
    s=Solution()
    l1=ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2=ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    print (s.addTwoNumbers(l1,l2).next.next.val)
