# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        def reverseList(head):
            prev= None
            current=head
            while current:
                next_node=current.next
                current.next=prev
                prev=current
                current=next_node
            return prev
        second_half=reverseList(slow)
        first_half=head
        second_half_copy=second_half
        while second_half_copy:
            if first_half.val != second_half_copy.val:
                return False
            first_half=first_half.next
            second_half_copy=second_half_copy.next
        reverseList(second_half)

        return True