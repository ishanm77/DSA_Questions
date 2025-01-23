
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None



class Solution:
    #Function to insert a new node at given position in doubly linked list.
    def addNode(self, head, p, x):
        if not head:
            return None
        current=head
        for i in range(p):
            if current is None:
                return head
            current = current.next
        newnode=Node(x)  
        
        newnode.next=current.next
        if current.next:
            current.next.prev=newnode
        current.next=newnode
        newnode.prev=current
        
        return head
