# your task is to complete this function

'''
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''
class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def getMiddle(self, head):
        # Code here
        # return the value stored in the middle node
        if head==None:
            return head
            
        # temp = head 
        # length=0
        # # Identify length of Linked LIst
        # while temp:
        #     length+=1
        #     temp=temp.next
            
        # # print(length)
        # length=(length//2)+1
        
        # temp=head
        # while length-1:
        #     length-=1
        #     temp=temp.next
            
        # return temp.data
        
        
        # Tortoise - Hare Method 
        
        slow_ptr=head
        fast_ptr=head
        
        while fast_ptr!=None and fast_ptr.next!=None:
            slow_ptr=slow_ptr.next
            fast_ptr=fast_ptr.next.next
            
        return slow_ptr.data