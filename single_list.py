class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
class LinkList:
    def __init__(self):
        self.head = None
    def Traversing(self,head):
        while head.next:
            print(.)