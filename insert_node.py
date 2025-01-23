   
class Node:
    def __init__(self,data):
        self.data=data

class Solution:
    #Function to insert a node at the end of the linked list.
    def insertAtEnd(self,head,x):
        newnode=Node(x)
        if not head:
            return newnode
        current=head
        while current.next:
            current=current.next
        current.next=newnode
        return head
