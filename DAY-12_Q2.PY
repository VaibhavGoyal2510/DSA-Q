#User function Template for python3

class Solution:
    def maxDepth(self, s):
        # Code here
        count_open = 0
        depth=0
        max1=0
        
        for ch in s:
            if ch == '(':
                count_open+=1
                max1+=1
            
            elif ch == ')':
                depth=max(max1,depth)
                count_open-=1
                max1=count_open
                
        return depth
            
            