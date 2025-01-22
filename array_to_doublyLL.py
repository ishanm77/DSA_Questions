
'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
	        self.prev = None
'''
class Solution:
    def constructDLL(self, arr):
        if not arr:
            return None
        head=Node(arr[0])
        current=head
        for val in arr[1:]:
            newnode=Node(val)
            current.next=newnode
            newnode.prev=current
            current=newnode
        return head
