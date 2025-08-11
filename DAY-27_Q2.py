'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def inOrder(self,root):
        # code here
        ans =[]
        
        def preorderr(root):
            if root==None:
                return 
            
            
            preorderr(root.left);
            ans.append(root.data)
            preorderr(root.right);
            
        preorderr(root)
        return ans