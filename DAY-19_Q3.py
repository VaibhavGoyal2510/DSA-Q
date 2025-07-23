
# your task is to complete this function
# function should return new head pointer

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

def deleteNode(head, x):
    # Code here
    if x==1:
        temp=head
        head=head.next
        temp.next=None
        return head
        
    temp = head
    while x-2:
        x-=1
        
        temp=temp.next
        
    # print(temp.data)
    temp.next=temp.next.next
    
    return head
        
        