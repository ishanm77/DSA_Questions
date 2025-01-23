'''
class DLLNode:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''

class Solution:
    def reverseDLL(self, head):
        if not head:
            return None
        current=head
        newhead=None
        while current:
            current.prev,current.next=current.next,current.prev
            newhead=current
            current=current.prev
        return newhead