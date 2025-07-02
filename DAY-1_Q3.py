# maxConsecBits
def maxConsecBits(self, arr):
        #code here 
        maxx=0
        temp=0
        context=arr[0]
        
        for num in arr:
            if num==context:
                temp+=1
                
            else:
                context=num
                maxx=max(maxx,temp)
                temp=1
            
        return max(maxx,temp)