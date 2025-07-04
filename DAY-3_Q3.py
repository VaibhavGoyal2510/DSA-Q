# Alternate Positive Negative


#User function Template for python3

class Solution:
    def rearrange(self,arr):
        # code here
        pos=[]
        neg=[]
        for num in arr:
            if num<0:
                neg.append(num)
                
            else:
                pos.append(num)
                
        
        length = len(neg) if len(neg)<=len(pos) else len(pos)
        
        for i in range(length):
            
            arr[2*i] = pos[i]
            arr[2*i+1]= neg[i]
            
        
        index = 2*length
        if len(pos)>len(neg):
            for i in range(length,len(pos)):
                arr[index]=pos[i]
                index+=1
                
        else :
            for i in range(length,len(neg)):
                arr[index]=neg[i]
                index+=1
                
        return arr
                
        
                
            
            