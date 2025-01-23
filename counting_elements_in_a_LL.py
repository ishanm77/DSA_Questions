
#Linked list class
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
       
class Solution:
    # Function to count nodes of a linked list.
    def getCount(self, head):
        length=0
        current=head
        
        while current:
            length+=1
            current=current.next
        return length