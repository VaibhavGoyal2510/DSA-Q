class Solution:
    def Search(self, arr, key):
        # code here
        # Pivot 
        
        left=0
        right=len(arr)-1 
        pivot =-1
        while left<=right:
            mid=(left+right)//2
            if mid<right and arr[mid]>arr[mid+1]:
                pivot = mid 
                break
                
            elif  mid>left and arr[mid]<arr[mid-1]:
                pivot=mid-1
                break
                
            elif arr[left]>=arr[mid]:
                right=mid-1
            
            else: 
                left=mid+1
                
        # print(pivot)
        
        
        # Our BS code 
        
        def BS(arr,left,right,k):
            if left>right:
                return False
            
            mid = (left+right)//2
            
            if arr[mid]==k:
                return mid
            
            elif arr[mid]>k:
                return BS(arr,left,mid-1,k)
                
            else:
                return BS(arr,mid+1,right,k)
                
                
        if pivot==-1:
            return BS(arr,0,len(arr)-1,key)
            
        if arr[pivot]==key:
            return pivot
            
        if key>arr[0]:
            return BS(arr,0,pivot,key)
            
        else:
            # print("eifj")
            return BS(arr,pivot+1,len(arr)-1,key)