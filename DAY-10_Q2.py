 #User function Template for python3
 
class Solution:
    
    # arr[] : the input array
    
    #Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self,arr):
    #     #code here
    #     # NlogN
    #     arr.sort()
    #     f=arr[0]
    #     l=1
    #     max_l=0
    #     for i in range(1,len(arr)):
    #         # print(f,arr[i])
    #         # print("len ",l,max_l)
    #         if arr[i]<=f+1:
    #             f+=1
    #             l+=1
    #         else:
    #             max_l=max(max_l,l)
    #             l=1
    #             f=arr[i]
                
    #     max_l=max(max_l,l)
    #     return max_l
    
        h=set()
        
        for num in arr:
            h.add(num)
            
        max_l=0
        for val in h:
            if val-1 not in h:
                temp=1
                while 1:
                    if val+1 in h:
                        temp+=1
                        val+=1
                    else:
                        break
                max_l=max(temp,max_l)
                
        return max_l
            
                
                