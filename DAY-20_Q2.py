#function Template for python3

"""
# Node Class

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""

class Solution:
    def reverseList(self, head):
        # Code here
        
        if head ==None:
            return head
            
        curr=head
        nex=None
        
        while curr !=None :
            # print(curr.data)
            temp = curr.next 
            curr.next = nex
            nex=curr
            head=curr
            curr=temp
            
        return head