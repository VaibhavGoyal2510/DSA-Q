#User function Template for python3


''' Node of a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def searchKey(self, n, head, key):
        #Code here
        if head ==None:
            return False
            
        temp = head 
        
        while temp:
            if temp.data==key:
                return True
            
            temp=temp.next
            
        return False