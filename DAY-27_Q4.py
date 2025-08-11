#Your task is to complete this function

class BST:
    
    #Function to search a node in BST.
    def search(self, node, x):
        #code here
        
        while node:
            if node.data==x:
                return 1
                
            if node.data>x:
                node=node.left
                
            else:
                node=node.right
                
                
        return 0