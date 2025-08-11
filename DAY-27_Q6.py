'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''
class Solution:
    def findMax(self,root):
        #code here
        while root.right:
            root=root.right
            
        return root.data
        
        
        
        
    def findMin(self,root):
        #code here
        while root.left:
            root=root.left
            
        return root.data