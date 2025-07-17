class Solution:
    def findKRotation(self, arr):
        # code here
        
        left =0 
        right= len(arr)-1
        
        pivot=-1
        
        while left<=right:
            mid =(left+right)//2
            
            if mid<right and arr[mid]>arr[mid+1]:
                return mid+1
                
            elif mid>left and arr[mid]<arr[mid-1]:
                return mid 
                
            elif arr[left]>arr[mid]:
                right=mid-1
                
            else:
                left=mid+1
                
        return pivot+1