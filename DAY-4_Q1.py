# Leaders in an array
class Solution:
    def leaders(self, arr):
        # code here
        
        maxx=0
        f=[]
        for i in range(len(arr)-1,-1,-1):
            # print(i)
            if arr[i]>=maxx:
                f.append(arr[i])
                maxx=arr[i]
                
        return f[::-1]
            