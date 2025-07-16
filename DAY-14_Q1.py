#User function Template for python3

class Solution:
    def searchInsertK(self, arr, N, k):
        # code here
        left=0
        right=N-1
        
        while left<=right:
            mid =(left+right)//2
            
            if arr[mid]==k:
                return mid
                
            elif arr[mid]>k:
                right=mid-1
                
            else:
                left=mid+1
                
            
            
        return left