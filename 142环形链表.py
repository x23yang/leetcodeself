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
        seen = set()
        temp = head 
        while temp:
            if temp not in seen:
                seen.add(temp)
            else:
                return temp
            temp = temp.next
        return -1
head = ListNode(1)
head.next = head
# head.next.next = ListNode(0)
# head.next.next.next = ListNode(-4)
#head.next.next.next.next = head.next
s = Solution()
res = s.detectCycle(head)
print(res)
while res: 
    print(res.val)
    res = res.next