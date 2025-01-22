class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
class Solution:
    def reverseList(self,head):
        prev=None
        current=head
        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        return prev
    
    def addOne(self,head):
        head=self.reverseList(head)
        current=head
        carry=1
        while current and carry:
            current.data +=carry
            carry=current.data//10
            current.data %=10
            if carry and not current.next:
                current.next=Node(0)
            current=current.next
        return self.reverseList(head)