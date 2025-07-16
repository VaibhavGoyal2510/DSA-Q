class Solution:
    def search(self,arr,key):
        # code here KYA HOGA BHAI , Kuch pata nahi ,
        # Har waqt lagta hai kuch aur kar liya jaye
        # Kis cheez mein man lagta hai ye bhi figured out nahi hai
        # aur mein 21 ka hu :)
        
        def BS(arr,left,right,t):
            if left>right:
                return -1
            mid =(left+right)//2
            
            if arr[mid]==t:
                return mid 
                
            elif arr[mid]>t:
                return BS(arr,left,mid-1,t)
                
            else:
                return BS(arr,mid+1,right,t)
            
        
        left =0 
        right =len(arr)-1
        pivot=-1
        # First find pivot
        while left<=right:
            mid = (left+right)//2
            
            if mid<right and arr[mid]>arr[mid+1]:
                pivot=mid
                break
            
            elif mid>left and arr[mid]<arr[mid-1]:
                pivot=mid-1
                break
            
            elif arr[left]>=arr[mid]:
                right=mid-1
                
            else:
                left=mid+1
                
                
        if pivot==-1:
            return BS(arr,0,len(arr)-1,key)
            
        if arr[pivot]==key:
            return pivot
            
        elif key>= arr[0]:
            return BS(arr,0,pivot-1,key)
            
        else:
            return BS(arr,pivot+1,len(arr)-1,key)
            
        
            
    
                
            