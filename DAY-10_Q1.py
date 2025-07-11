class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        # left=0
        # right=0
        # has={}
        # sum1=0
        # max_sum=float('-inf')
        
        # while right<len(arr):
        #     sum1+=arr[right]
        #     has[sum1] = has.get(sum1,right)
        #     if sum1>max_sum:
        #         max_sum=sum1
                
        #     else:
        #         x= sum1-arr[right]
        #         if x not in has:
        #             sum1-=arr[left]
        #             left+=1
                    
        #     print("sum is ",sum1)
        #     right+=1
          
        # print(has)  
        # return max_sum
        
        
        
        # Kadane's Algorithm 
        sum1=0
        max_sum=float('-inf')
        
        for num in arr:
            sum1+=num
            
            if sum1>max_sum:
                max_sum=sum1
                
            if sum1<0:
                sum1=0
                
        return max_sum
            
            
            