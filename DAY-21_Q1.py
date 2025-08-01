# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==1:
            return head
            
        temp = head
        left=None
        
        final_head=None
        f=0
        prev=None
        
        while temp:
            if int(temp.data)%2==0:
        
                if f==1:
                    if final_head==None:
                        final_head=temp
                        
                    prev.next=temp.next
                    
                    temp.next=head
                    
                    
                    if left:
                        left.next=temp
                    
                    left=temp
                    
                    
                    temp=prev.next
                    continue
                else:
                    
                    if final_head==None:
                        final_head=head
                    head=head.next
                    left=temp
                
            else:
                f=1
                
                
            
            prev = temp
            temp=temp.next
            
            
        # print("Count is ",count)
        return final_head if final_head!=None else head
        