'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self, head):
        #code here
        
        if head == None:
            return 0
            
        ptr = head 
        f=0
        while ptr!=None and ptr.next!=None:
            if ptr.data>0:
                ptr.data=-1*ptr.data
                
            else:
                ptr.data=-1*ptr.data
                f=1
                break
            
            ptr=ptr.next
            
        if f==0:
            return 0
            
        count=1
        ptr=ptr.next
        while ptr.data<0:
            count+=1
            ptr=ptr.next
            
        return count