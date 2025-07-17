#User function Template for python3

class Solution:
    def findMin(self, arr):
        #complete the function here
        
        left =0 
        right = len(arr)-1
        t=arr[0]
        
        while left<=right:
            
            mid = (left+right)//2
            
            if mid<right and arr[mid]>arr[mid+1]:
                return arr[mid+1]
                
            elif mid>left and arr[mid]<arr[mid-1]:
                return arr[mid]
                
            elif arr[left]>arr[mid]:
                right=mid-1
            else:
                left=mid+1
                
        return arr[0]