class Solution:
    def majorityElement(self, arr):
        #code here
        # O(n) space
        # seen={}
        
        # for num in arr:
        #     seen[num] = seen.get(num,0)+1
            
        # # print(seen)
        # k = len(arr)//2
        
        # for key,val in zip(seen,seen.values()):
        #     if val > k:
        #         return key
                
        # return -1
        
        # Moore's Voting Algo
        candidate =None
        count=0
        
        for num in arr:
            if count==0:
                candidate=num
                count+=1
                
            elif candidate == num:
                count+=1
                
            else:
                count-=1
            
            # print(count)
            
        if arr.count(candidate) > len(arr)//2:
            return candidate
            
        return -1