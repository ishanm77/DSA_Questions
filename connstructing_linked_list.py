'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
'''
class Solution:
    def constructLL(self, arr):
        if not arr:
            return None
        head=Node(arr[0])
        current=head
        for val in arr[1:]:
            current.next=Node(val)
            current=current.next
        return head