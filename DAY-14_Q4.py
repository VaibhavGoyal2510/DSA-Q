class Solution:
    def countFreq(self, arr, target):
        #code here
        left=0
        right= len(arr)-1
        
        while left<=right:
            mid=(left+right)//2
            if arr[mid]==target:
                count=0
                temp=mid
                while temp>=0 and arr[temp]==target:
                    count+=1
                    temp-=1
                    
                while mid<len(arr) and arr[mid]==target:
                    count+=1
                    mid+=1
                return count-1
                
            elif arr[mid]>target:
                right=mid-1
                
            else:
                left=mid+1
                
        return 0