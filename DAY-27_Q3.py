'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    #Function to return a list containing the postorder traversal of the tree.
    def postOrder(self, root):
        # code here
        ans =[]
        
        def preorderr(root):
            if root==None:
                return 
            
            
            preorderr(root.left);
            preorderr(root.right);
            ans.append(root.data)
            
        preorderr(root)
        return ans