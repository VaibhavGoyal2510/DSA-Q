# Your task is to complete this function
# function should add a new node after the pth position
# function shouldn't print or return any data

'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

'''

class Solution:
    #Function to insert a new node at given position in doubly linked list.
    def addNode(self, head, p, x):
        # Code here
            
        if head == None:
            return Node(x)
            
        temp=head
        
        while p:
            p-=1
            temp=temp.next
            
        # print(temp.data)
            
        newnode = Node(x)
        newnode.next=temp.next
        newnode.prev=temp
        temp.next=newnode
        
        return head