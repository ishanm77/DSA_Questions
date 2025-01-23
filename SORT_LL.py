# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        nodes=[]
        current=head
        while current:
            nodes.append(current.val)
            current=current.next
        nodes.sort()
        dummy=ListNode(0)
        current=dummy
        for val in nodes:
            current.next=ListNode(val)
            current=current.next
        return dummy.next