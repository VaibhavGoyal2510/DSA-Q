'''
class DLLNode:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''

class Solution:
    def reverseDLL(self, head):
        if head is None or head.next is None:
            return head
        #return head of reverse doubly linked list
        curr=head
        prev=None
        # last=head
        while curr:
            
            curr.prev,curr.next=curr.next,curr.prev
            
            prev=curr
            curr=curr.prev
            # temp=temp.next
        
        
        return prev