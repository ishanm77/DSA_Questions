# Structure of node

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None


class Solution:
    def countNodesInLoop(self, head):
        if not head or not head.next:
            return 0
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                count = 1
                current = slow
                while current.next != slow:
                    current = current.next
                    count += 1
                return count
            
        return 0