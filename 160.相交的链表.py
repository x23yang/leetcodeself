# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA==None or headB == None:
            return None
        point_a = headA
        point_b = headB
        flag_a = 1
        flag_b = 1
        while True:
            if point_a == point_b:
                return point_a

            if point_a == None and flag_a:
                point_a = headB
                flag_a = 0
            else:
                point_a = point_a.next

            if point_b == None and flag_b:
                point_b = headA
                flag_b = 0
            else:
                point_b = point_b.next
                
            if point_a ==None and flag_a ==0 and point_b==None and flag_b ==0:
                return None

if __name__ =='__main__':
    s=Solution()
    gg = ListNode(1)
    gg.next =ListNode(8)
    gg.next.next = ListNode(4)
    gg.next.next.next = ListNode(5)
    headA = ListNode(4)
    headA.next = gg
    headB = ListNode(5)
    headB.next = ListNode(0)
    headB.next.next = gg
    temp = s.getIntersectionNode(headA,headB)
    while temp:
        print(temp.val)
        temp = temp.next
    

        
        