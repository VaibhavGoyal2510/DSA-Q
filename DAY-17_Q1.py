
from collections import defaultdict
class Solution:
    def cntSubarrays(self, arr, k):
        # code here
        
        sum1=0
        count=0
        has=defaultdict(int)
        has[0]=1
        for i in range(len(arr)):
            sum1+=arr[i]
            x= sum1-k
            count+=has[x]
            has[sum1]+=1
        return count