from typing import Optional


from typing import List
# from typing import Node

# Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None

# You can also use the following for printing the link list.
# displayList(node)

class Solution:
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        start=head
        end=head
        while end.next:
            end=end.next
        pairs=[]
        while start!=end and end.next!=start:
            sum=start.data+end.data
            if sum==target:
                pairs.append((start.data,end.data))
                start=start.next
                end=end.prev
            elif sum<target:
                start=start.next
            else:
                end=end.prev
        return pairs
        