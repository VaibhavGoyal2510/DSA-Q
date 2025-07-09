#  Next Permutation 
class Solution:
    def nextPermutation(self, arr):
        # code here
        min1=-1
        
        for i in range(len(arr)-1,-1,-1):
            if arr[i]>arr[i-1]:
                min1=i-1
                break
            
        # print(min1)
        # print(arr[::-1])
        if min1==-1:
            arr[0:len(arr)]=arr[0:len(arr)][::-1]
            return arr
            
        rev=-1
        
        for i in range(len(arr)-1,-1,-1):
            if arr[i]>arr[min1]:
                arr[i],arr[min1]=arr[min1],arr[i]
                rev=min1+1
                break
            
        # print(arr,rev)
        arr[rev:len(arr)] = arr[rev:len(arr)][::-1]
        return arr
            
        