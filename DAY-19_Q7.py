class Solution:
    def delete_node(self, head, x):
        #code here
        if head == None:
            return head
            
        if x==1:
            temp=head
            head=head.next
            head.prev=None
            temp.next=None
            return head
            
        temp = head 
        while x-1:
            x-=1
            
            temp=temp.next
            
        # print(temp.data)
        if temp.next==None:
            temp=temp.prev
            temp.next=None
            return head
            
        temp2=temp.prev
        temp2.next=temp.next
        
        temp=temp.next
        temp.prev=temp2
        
        return head
            
        