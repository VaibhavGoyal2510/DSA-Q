class Solution:
    def findOnce(self,arr):
        # Complete this function
        
        if len(arr)==1:
            return arr[0]
            
        if arr[0]!=arr[1]:
            return arr[0]
            
        if arr[len(arr)-1]!= arr[len(arr)-2]:
            return arr[len(arr)-1]
        
        left =0
        right=len(arr)-1
        
        while left<=right:
            mid=(left+right)//2
            
            if arr[mid]!= arr[mid+1] and arr[mid-1]!= arr[mid]:
                return arr[mid]
                
            elif (mid%2==0 and arr[mid]==arr[mid+1]) or (mid%2==1 and arr[mid-1]==arr[mid]):
                left=mid+1
                
            else:
                right=mid-1
                
        