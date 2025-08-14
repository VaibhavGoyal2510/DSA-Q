class Solution:
    def checkKthBit(self, n, k):
        # code here
        
        num=2**k
        
        ans = num^n
        
        if ans<n:
            return True
            
        return False
        