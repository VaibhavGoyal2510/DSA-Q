# Plus One 
def addOne(self, arr):
        # code here
        n=len(arr)
        for i in range(n-1,-1,-1):
            # print(i)
            if arr[i]<9:
                arr[i]+=1
                
                return arr
            
            arr[i]=0
            
        return [1]+arr