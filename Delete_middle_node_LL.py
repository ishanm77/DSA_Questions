# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        if not head or not head.next:
            return None
        slow=head
        fast=head
        prev=None
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        if prev:
            prev.next=slow.next
        return head