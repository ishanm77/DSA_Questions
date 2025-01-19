
# Node Class
class Node:
	def __init__(self, data):   # data -> value stored in node
		self.data = data
		self.next = None
		self.prev = None

class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        if not head :
            return head  #Empty list
        current=head
        while current and current.next:
            if current.data==current.next.data:
                duplicate=current.next     #remove duplicates
                current.next=duplicate.next
                if duplicate.next:      #update the prev pointer of the next node
                    duplicate.next.prev=current
                del duplicate    #free the memory
            else:       #move to the next node
                current=current.next
        return head