class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self, arr, x):
        #Your code here
        left =0
        right=len(arr)-1
        
        while left<=right:
            mid = (left+right)//2
            
            if arr[mid]==x:
                while mid<len(arr) and arr[mid]==x:
                    mid+=1
                return mid-1
                
            elif arr[mid]>x:
                right=mid-1
                
            else:
                left=mid+1
                
        return right
        