'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def preorder(self,root):
    # code here
    
        ans =[]
        
        def preorderr(root):
            if root==None:
                return 
            
            ans.append(root.data)
            
            preorderr(root.left);
            preorderr(root.right);
            
        preorderr(root)
        return ans