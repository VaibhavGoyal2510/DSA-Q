class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # code here
        # c1=0 #for 0
        # c2=0 #for 1
        # c3=0 #for 2
        
        # for num in arr:
        #     if num==0:
        #         c1+=1
                
        #     elif num==1:
        #         c2+=1
                
        #     else:
        #         c3+=1
                
                
        # for i in range(len(arr)):
        #     if c1!=0:
        #         arr[i]=0
        #         c1-=1
                
        #     elif c2!=0:
        #         arr[i]=1
        #         c2-=1
                
        #     else:
        #         arr[i]=2
        #         c3-=1
        
        
        # Dutch National Flag Algorithm
        
        low=0
        mid=0
        high=len(arr)-1
        
        while mid<=high:
            if arr[mid]==1:
                mid+=1
                
            elif arr[mid]==0:
                arr[mid],arr[low]=arr[low],arr[mid]
                mid+=1
                low+=1
                
            elif arr[mid]==2:
                arr[mid],arr[high]=arr[high],arr[mid]
                high-=1
                
        return arr
            
            
            
        