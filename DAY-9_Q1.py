# User function Template for python3
# Longest Subarray with Sum K
class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        # Better solution using hashMap & best for this as +ve & -ve nums are there
        
        sum1=0
        max_len=0
        has={}
        left=0
        right=0
        while right<len(arr):
            # print(sum1,max_len)
            sum1+=arr[right]
            
            has[sum1] = has.get(sum1,right)
            
            if sum1==k:
                max_len=max(max_len,right-left+1)
            
            else:
                x = sum1-k
                
                if x in has:
                    index=has.get(x)
                    # print("OOye",right , index)
                    max_len=max(max_len,right-index)
                    
            right+=1
        # print(has)
        return max_len
            
            
        
        
        
        
        
        
        
        
        # Below is Optimal when only +ve nums are there
        
        # left=0
        # right=0
        # max_len=0
        # sum1=0
        
        # while right<len(arr):
        #     sum1+=arr[right]
        #     print(sum1,max_len)
        #     if sum1>k:
        #         sum1-=arr[left]
        #         left+=1
                
        #     while sum1!=k and right==len(arr)-1 and left>=0:
        #         left-=1
        #         sum1+=arr[left]
                
        #     if sum1==k:
        #         max_len=max(max_len,right-left+1)
                
                
        #     right+=1
            
        # return max_len
            
    
