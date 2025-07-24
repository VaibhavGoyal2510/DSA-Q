# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
            
        ptr = head
        
        while ptr!=None and ptr.next!=None:
            
            if ptr.val>0:
                ptr.val=-1*ptr.val
                
            else:
                ptr.val=-1*ptr.val
                return ptr
                
            ptr=ptr.next
            
        return None
        