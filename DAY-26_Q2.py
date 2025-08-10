#Back-end complete function Template for Python 3

'''
# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
		        self.prev = None
'''
class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        # return head after editing list
        context = head
        
        temp = head.next
        
        while temp:
            if temp.data==context.data:
                context.next=temp.next
                k=temp.next
                if k: k.prev=temp.prev
                
            else:
                context=temp
                
            temp=temp.next
            
        return head
                