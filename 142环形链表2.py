class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return 
        fast = head 
        slow = head 
        if fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        else:
            return 
        while fast != slow:
            if fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            else:
                return 
        slow = head 
        while fast != slow:
            slow = slow.next
            fast = fast.next
        return slow
head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(0)
# head.next.next.next = ListNode(-4)
# head.next.next.next.next = head.next
s = Solution()
res = s.detectCycle(head)
print(res)
while res: 
    print(res.val)
    res = res.next
