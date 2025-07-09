class Solution:
    def findUnique(self, arr):
        # code here
        ans=0
        for num in arr:
            ans^=num
        
        return ans