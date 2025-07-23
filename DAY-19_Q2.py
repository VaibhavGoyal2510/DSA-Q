'''    
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
class Solution:
    def insertAtEnd(self, head, x):
        #code here 
        if head==None:
            return Node(x)
        temp = head
        
        
        while temp.next:
            # if temp:
            temp=temp.next
        
    # print(temp.data)
        # newnode = 
        temp.next = Node(x)
            
        
        return head