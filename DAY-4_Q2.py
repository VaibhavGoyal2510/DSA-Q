#User function Template for python3
# Q is Missing And Repeating
class Solution:
    def findTwoElement( self,arr): 
        # code here
    
        # has = [0] *(len(arr)+1)
        
        # for i in range(len(arr)):
        #     has[arr[i]]+=1
            
        # # print(has)
        
        # ans1=-1
        # ans2=-1
        # for i in range(1,len(has)):
        #     if has[i]>1:
        #         ans1=i
            
        #     elif has[i]==0:
        #         ans2=i
        
        # return [ans1,ans2]
        
        
        
        # O(1) Space Solution 
        
        repeat =-1
        miss =-1 
        
        for i in range(len(arr)):
            val = abs(arr[i])
            
            if (arr[val-1])>0:
                arr[val-1]*=-1
                
            else:
                repeat = val
            
        for i in range(len(arr)):
            if arr[i]>0:
                miss = i+1
                break
            
        return [repeat,miss]
 
