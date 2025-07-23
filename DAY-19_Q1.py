class Solution:
    def floorSqrt(self, n): 
    # code here
    # BRUTE FORCE - O(N) , Space -> O(1)
        # ans=0
        # for i in range(1,n+1):
        #     val=i*i
            
        #     if val<=n:
        #         ans=i
                
        #     else: break
        
        # return ans
        
        low =1
        high = n
        # ans=0
        while low<=high:
            mid=(low+high)//2
            val = mid*mid
            if val<=n:
                # ans=mid
                low=mid+1
                
            else:
                high=mid-1
                
        return high